import numpy as np
from multiprocessing import pool


global_map = []
max_value_dict = {}
max_value_assemble_plan = {}

calibration_point = (18.528956, -67.216985)
x_max = 170
y_max = 40
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
    def __init__(self, location, packet_group):
        self.location = location
        self.packet_group = packet_group


def init_city():
    global city_list
    Fajardo = City([165, 21], {"type1":[[1, 0, 1]], "type2":5})
    SanPablo = City([112, 13], {"type1":[[2, 0, 0], [2, 0, 0], [0, 0, 2]], "type2":7})
    SanJuan = City([120, 12], {"type1":[[0, 4, 0], [2, 0, 0], [2, 0, 0]], "type2":5})
    Bayamon = City([112, 15], {"type1":[[2, 0, 0], [2, 0, 0], [2, 0, 0], [2, 0, 0], [0, 4, 0], [0, 0, 2], [0, 0, 2], [0, 0, 2], [0, 0, 2]], "type2":12})
    Arecibo = City([50, 9.5], {"type1":[[2, 0, 0]], "type2":2})

    city_list = [Fajardo, SanPablo, SanJuan, Bayamon, Arecibo]


def init_global_map():
    global global_map
    for i in np.arange(0, x_max, 2.5):
        for j in np.arange(0, y_max, 2.5):
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


def get_value_function():
    pass


def get_pair_of_drone_and_packet(city, distance):
    pass


def get_access_city_list(container_location):
    ret = {}
    for city in city_list:
        ret[city] = []
        for drone in drone_list:
            if distance(container_location, city.location) < (min_fly_distance(drone) * min_fly_distance(drone)):
                ret[city].append(drone)

    return ret


def dynamic_programming_for_max_value_function(container_1, container_2, container_3):
    val_1 = 0
    val_2 = 0
    val_3 = 0

    aval_list_1 = get_access_city_list(container_1)
    aval_list_2 = get_access_city_list(container_2)
    aval_list_3 = get_access_city_list(container_3)

    if len(aval_list_1) == 0 or len(aval_list_2) == 0 or len(aval_list_3) == 0:
        max_value_dict[str(container_1, container_2, container_3)] = 0
    else:
        for


if __name__ == '__main__':
    init_global_map()
    init_city()

    task_pool = pool.Pool()

    for container_1 in global_map:
        if container_1[0] < 40:
            map_2 = simplify_map(global_map, [container_1])
            for container_2 in map_2:
                if container_2[0] - container_1[0] < 60:
                    map_3 = simplify_map(global_map, [container_1, container_2])
                    for container_3 in map_3:
                        task_pool.map(printPoint, [container_1, container_2, container_3])
                else:
                    break
        else:
            break
    task_pool.close()
    task_pool.join()
