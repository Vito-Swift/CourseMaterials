import numpy as np
import json
import time
import multiprocessing

cargo_1 = 0.125
cargo_2 = 1

global_map = []
max_value_dict = {}
max_value_assemble_plan = {}

calibration_point = (18.528956, -67.216985)
x_max = 170
y_max = 30
min_distance_between = 45

container_val = 168
b_val = 1.5
c_val = 9
d_val = 1.5
e_val = 1.5
f_val = 3
g_val = 1.5

drone_list = {
    "B": (b_val, "type1", 8, 79, 40),
    "C": (c_val, "type2", 14, 64, 35),
    "D": (d_val, "type1", 11, 60, 18),
    "E": (e_val, "type2", 15, 60, 15),
    "F": (f_val, "type2", 22, 79, 24),
    "G": (g_val, "type2", 20, 64, 16),
}

drone_val_index = 0
drone_type_index = 1
drone_cap_index = 2
drone_spd_index = 3
drone_flight_time_index = 4

drone_t2_list = ("C", "E", "F", "G")
drone_t1_list = ("B", "D")

city_list = []


class City:
    def __init__(self, location, packet_group, time_count, name):
        self.location = location
        self.packet_group = packet_group
        self.time_count = time_count
        self.name = name

    def __str__(self):
        return str(self.name)


def init_city():
    global city_list
    Fajardo = City([165, 21], {"type1":[[1, 0, 1]], "type2":5}, 1, "Fajardo")
    SanPablo = City([112, 13], {"type1":[[2, 0, 0], [2, 0, 0], [0, 0, 2]], "type2":7}, 2, "SanPablo")
    SanJuan = City([120, 12], {"type1":[[0, 4, 0], [2, 0, 0], [2, 0, 0]], "type2":5}, 2, "SanJuan")
    Bayamon = City([112, 15], {"type1":[[2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [0, 4, 0], [0, 0, 2], [0, 0, 2], [0, 0, 2], [0, 0, 2]], "type2":12}, 4, "Bayamon")
    Arecibo = City([50, 9.5], {"type1":[[2, 0, 0]], "type2":2}, 2, "Arecibo")

    city_list = [Fajardo, SanPablo, SanJuan, Bayamon, Arecibo]


def init_global_map():
    global global_map
    for i in np.arange(0, x_max, 5):
        for j in np.arange(0, y_max, 5):
            global_map.append([i, j])


def simplify_map(init_map, settled_point):
    ret_map = eval(str(init_map))
    for p in settled_point:
        for point in ret_map:
            if distance(p, point) < (min_distance_between*min_distance_between):
                ret_map.pop(ret_map.index(point))
    return ret_map


def distance(p_0, p_1):
    return (p_0[0]-p_1[0])*(p_0[0]-p_1[0])+(p_0[1]-p_1[1])*(p_0[1]-p_1[1])


def min_fly_distance(drone_type):
    return 0.5 * drone_list[drone_type][drone_flight_time_index] * drone_list[drone_type][drone_spd_index]


def get_access_city_list(container_location):
    ret = {}
    for city in city_list:
        ret[city] = []
        for drone in drone_list:
            if distance(container_location, city.location) < (min_fly_distance(drone) * min_fly_distance(drone)):
                ret[city].append(drone)

    return ret


def local_max_value_function(container_location, aval_city_list):
    city_distance_list = {}
    for city in aval_city_list:
        city_distance_list[str(city)] = distance(p_0=container_location, p_1=city.location)

    max_value = local_recursive(aval_city_list, 0, city_distance_list, [])

    return max_value


def local_recursive(aval_city_list, current_val, distance_list, track_stat):
    if current_val > container_val:
        return local_value_function(aval_city_list, distance_list, track_stat)
    else:
        test_local_value_list = []
        for city in aval_city_list:
            if distance_list[str(city)] < 300:
                for drone in drone_t2_list:
                    if drone in aval_city_list[city]:
                        time_count = (((drone_list[drone][drone_spd_index]*drone_list[drone][drone_flight_time_index] * 0.75 / distance_list[city]) // 2) + 1) * (drone_list[drone][drone_cap_index]//city.packet_group["type2"])
                        new_track = eval(str(track_stat))
                        new_track.append([str(city), time_count])
                        new_value = local_recursive(aval_city_list, current_val + drone_list[drone][drone_val_index] + cargo_2, distance_list, new_track)
                        test_local_value_list.append(new_value)
            else:
                for drone in drone_t1_list:
                    time_count = city.time_count
                    new_track = eval(str(track_stat))
                    new_track.append([str(city), time_count])
                    new_value = local_recursive(aval_city_list, current_val+(drone_list[drone][drone_val_index]+cargo_1)*len(city.packet_group), distance_list, new_track)
                    test_local_value_list.append(new_value)

        return max(test_local_value_list)


# Track Stat: [destination, pair_count]
def local_value_function(aval_city_list, distance_list, track_stat):
    dic = {}
    for city in aval_city_list:
        dic[city] = 0

    for pack in track_stat:
        if distance_list[pack[0]] < 300:
            dic[pack[0]] += pack[1]

    l = [dic[i] for i in dic]
    k = np.var(l)
    if k < 0.1:
        k = 10
    else:
        k = 1/np.var(l)

    return k + 0.5*(np.mean(l))


def dynamic_programming_for_max_value_function(container_1, container_2, container_3):
    aval_list_1 = get_access_city_list(container_1)
    aval_list_2 = get_access_city_list(container_2)
    aval_list_3 = get_access_city_list(container_3)

    max_value_dict[str([container_1, container_2, container_3])] = 0

    if len(aval_list_1) == 0 or len(aval_list_2) == 0 or len(aval_list_3) == 0:
        pass
    else:
        max_value_1 = local_max_value_function(container_1, aval_list_1)
        max_value_2 = local_max_value_function(container_2, aval_list_2)
        max_value_3 = local_max_value_function(container_3, aval_list_3)
        max_value_dict[str([container_1, container_2, container_3])] = max_value_1+max_value_2+max_value_3

    print("finished")


def simulation_finished():
    with open("./simLocation"+str(int(time.time()))+".txt", 'w') as file:
        file.write(json.dumps(max_value_dict))

    print("Simulation Completed!")


if __name__ == '__main__':
    init_global_map()
    init_city()
    task_pool = []

    for container_1 in global_map:
        if abs(container_1[0]) < 35:
            map_2 = simplify_map(global_map, [container_1])
            for container_2 in map_2:
                if abs(container_2[0] - container_1[0]) > 20 or abs(container_2[0] - container_1[0]) < 50:
                    map_3 = simplify_map(global_map, [container_1, container_2])
                    for container_3 in map_3:
                        p = multiprocessing.Process(target=dynamic_programming_for_max_value_function, args=(container_1, container_2, container_3))
                        task_pool.append(p)
                        p.start()
                else:
                    break
        else:
            break

    for process in task_pool:
        process.join()

    simulation_finished()
