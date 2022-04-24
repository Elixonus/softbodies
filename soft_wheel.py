from copy import deepcopy
from vectors import Vector
from structures import Wheel
from render import render

wheel = Wheel(position=Vector(0, 0), radius=0.5, rings=3, slices=10, mass=1, stiffness=100, dampening=1)
nodes = wheel.nodes
links = wheel.links

frames = []

for i in range(100):
    for s in range(1):
        for node in nodes:
            node.force.set(Vector(0, -9.80665 * node.mass))
        for link in links:
            link.nodes[0].force.add(link.get_force() * (link.nodes[0].position - link.nodes[1].position) / Vector.dist(
                link.nodes[0].position, link.nodes[1].position))
            link.nodes[1].force.add(link.get_force() * (link.nodes[1].position - link.nodes[0].position) / Vector.dist(
                link.nodes[0].position, link.nodes[1].position))

        nodes[0].force.set(Vector(0, 0))

        for node in nodes:
            node.iterate(time=0.005)

    if i % 50 == 0:
        frame = deepcopy((nodes, links))
        frames.append(frame)

render(frames, camera_position=Vector(0, 0), camera_zoom=0.5)