from plotter import Plotter
from hopfield import HopfieldNet
from data_storage import DataStorage
from input import distance_matrix, normalize, normalize_cords
import subprocess as sp
import datetime as dt
import os
import time
import sys


def generate_images(new_path, seed, dataPointRange, freq, cords, dataStorage):
    print("Generating images!")

    for dataPointIndex in range(0, dataPointRange):
        plot_data_point(new_path,
                        dataStorage.get_net_configuration(seed),
                        dataStorage.get_data_point(seed, dataPointIndex),
                        dataPointIndex,
                        freq,
                        cords)
        sys.stdout.write(f"Image {dataPointIndex} out of {dataPointRange}\r")
    print("It is done")


def get_map(acts, cords):
    points = []
    for pos in range(0, len(acts)):
        for city in range(0, len(acts)):
            if (acts[city][pos] > 0.75):
                points.append(cords[city])
    return points


def plot_data_point(new_path, netConfiguration, netState, imgIndex, freq, cords):
    plotter = Plotter()
    plotter.add_subplot(netState["activations"], 'hot', 0, 1, f"Activations {imgIndex * freq}")
    plotter.add_subplot(netState["inputs"], 'coolwarm', -0.05, 0.05, f"Inputs {imgIndex * freq}")
    plotter.add_subplot(
        netState["inputsChange"], 'bwr', -0.001, 0.001, f"Inputs changes {imgIndex * freq}")
    plotter.add_graph(get_map(netState["activations"], cords))
    plotter.plot(
        f"seed 1; a {netConfiguration['a']}; b {netConfiguration['b']}; c {netConfiguration['c']}; "
        f"d {netConfiguration['d']}; size_adj"
        f" {netConfiguration['size_adj']}; u0 {netConfiguration['u0']}; "
        f"timestep {netConfiguration['timestep']};",
        f"{new_path}\img{imgIndex}.png")


def run(seed, steps, size_adj, data, freq):
    distances = distance_matrix(data)
    normalized_distances = normalize(distances)
    normalized_cords = normalize_cords(data)

    data_storage = DataStorage()

    net = HopfieldNet(normalized_distances, seed, size_adj)

    date = dt.datetime.now().strftime("%H-%M-%S_%d-%m-%Y")
    new_path = f"..\\plots\\{date}-seed{seed}-steps{steps}\\"
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        print(f"Created log directory: {new_path}")

    old = time.time()
    print(time.time() - old)
    data_storage.start_new_seed(seed, net.get_net_configuration())
    step = 0
    img = 0
    for step in range(0, steps):
        print(f"time {time.time() - old}")
        old = time.time()
        net.update()
        step += 1
        print(f"Update iter: {step}")

        if step % freq == 0:
            data_storage.save_data_point(net.get_net_state(), img)
            img += 1

    generate_images(new_path, seed, int(steps / freq), freq, normalized_cords, data_storage)
    ffmpeg_command = f"ffmpeg -r 10 -i {new_path}img%d.png -vframes {int(steps/freq)} " \
                     f"{new_path}run.mp4"
    print(ffmpeg_command)
    sp.call(ffmpeg_command)
    open(f"{new_path}\Success", "w")
