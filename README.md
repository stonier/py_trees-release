# Py Trees

[[About](#about)][[Status](#status)][[Demos & Tutorials](#demos-and-tutorials)][[Installation](#installation)][[PyTrees-Ros Ecosystem](#pytrees-ros-ecosystem)]

----

## About

PyTrees is a python implementation of behaviour trees designed to facilitate the rapid development of medium sized decision making engines for use in fields like robotics. Brief feature list:

* Sequence, Selector, Parallel and Chooser composites
* Blackboards for data sharing
* Python generators for smarter ticking over the tree graph
* Python decorators for enabling meta behaviours
* Render trees to dot graphs or visualise with ascii graphs on stdout

## Docs and Demos

[![devel][docs-devel-image]][docs-devel] [![1.2.x][docs-1.2.x-image]][docs-1.2.x] [![0.6.x][docs-0.6.x-image]][docs-0.6.x]

## Status

| | Devel | 1.2.x | 0.6.x | 0.5.x |
|:---:|:---:|:---:|:---:|:---:|
| Sources | [![devel][sources-devel-image]][sources-devel] | [![1.2.x][sources-1.2.x-image]][sources-1.2.x] | [![0.6.x][sources-0.6.x-image]][sources-0.6.x] | [![0.5.x][sources-0.5.x-image]][sources-0.5.x]
| Compatibility | [![Python 3.6][python36-image]][python36-docs] | [![Python 3.6][python36-image]][python36-docs] | [![Python 2.7][python27-image]][python27-docs] | [![Python 2.7][python27-image]][python27-docs] |
| Continuous Integration | [![devel-Status][devel-build-status-image]][devel-build-status] | [![1.2.x-Status][1.2.x-build-status-image]][1.2.x-build-status] | [![melodic-Status][melodic-build-status-image]][melodic-build-status] | [![kinetic-Status][kinetic-build-status-image]][kinetic-build-status] | |
| Documentation | [![devel-Docs][rtd-devel-image]][docs-devel] | [![1.2.x-Docs][rtd-1.2.x-image]][docs-1.2.x] | [![0.6.x-Docs][rtd-0.6.x-image]][docs-0.6.x] | ![0.5.x-Docs][not-available-docs-image] | |

## Installation

From [ppa](https://launchpad.net/~d-stonier/+archive/ubuntu/snorriheim) on Ubuntu/Bionic:

```
$ sudo apt install python3-py-trees
```

From [pypi](https://pypi.python.org/pypi/py_trees):

```
$ pip install py_trees
```

In a Python Virtual Environment:

```
$ git clone https://github.com/splintered-reality/py_trees
$ cd py_trees
$ source ./virtualenv.bash
```

Build your own python3 deb:

```
$ git clone https://github.com/splintered-reality/py_trees
$ cd py_trees
$ source ./virtualenv.bash
$ make deb
```

From the ROS2 ecosystem:

```
$ sudo apt install ros-<rosdistro>-py-trees
```

## PyTrees-ROS Ecosystem

See the `py_trees_ros` [README](https://github.com/splintered-reality/py_trees_ros/blob/devel/README.md) for the latest information on pytrees packages in the ROS ecosystem and their status.


[license-image]: https://img.shields.io/badge/License-BSD%203--Clause-orange.svg?style=plastic
[license]: LICENSE

[python36-image]: https://img.shields.io/badge/python-3.6-green.svg?style=plastic
[python36-docs]: https://docs.python.org/3.6/ 
[python27-image]: https://img.shields.io/badge/python-2.7-green.svg?style=plastic
[python27-docs]: https://docs.python.org/2.7/ 

[devel-build-status-image]: http://build.ros.org/job/Mbin_uB64__py_trees__ubuntu_bionic_amd64__binary/badge/icon?style=plastic
[devel-build-status]: https://circleci.com/gh/splintered-reality/py_trees/tree/devel
[1.2.x-build-status-image]: http://build.ros.org/job/Mbin_uB64__py_trees__ubuntu_bionic_amd64__binary/badge/icon?style=plastic
[1.2.x-build-status]: https://circleci.com/gh/splintered-reality/py_trees/tree/release/1.2.x
[crystal-build-status-image]: http://build.ros2.org/view/Cbin_uB64/job/Cbin_uB64__py_trees__ubuntu_bionic_amd64__binary/badge/icon?style=plastic 
[crystal-build-status]: http://build.ros2.org/view/Cbin_uB64/job/Cbin_uB64__py_trees__ubuntu_bionic_amd64__binary/
[melodic-build-status-image]: http://build.ros.org/job/Mbin_uB64__py_trees__ubuntu_bionic_amd64__binary/badge/icon?style=plastic
[melodic-build-status]: http://build.ros.org/job/Mbin_uX64__py_trees__ubuntu_bionic_amd64__binary
[kinetic-build-status-image]: http://build.ros.org/job/Kbin_uX64__py_trees__ubuntu_xenial_amd64__binary/badge/icon?style=plastic
[kinetic-build-status]: http://build.ros.org/job/Kbin_uX64__py_trees__ubuntu_xenial_amd64__binary

[docs-devel]: http://py-trees.readthedocs.io/
[docs-1.2.x]: http://py-trees.readthedocs.io/en/release-1.2.x/
[docs-0.6.x]: http://py-trees.readthedocs.io/en/release-0.6.x/
[docs-0.5.x]: http://docs.ros.org/kinetic/api/py_trees/html/

[docs-devel-image]: http://img.shields.io/badge/docs-devel-brightgreen.svg?style=plastic
[docs-1.2.x-image]: http://img.shields.io/badge/docs-1.2.x-brightgreen.svg?style=plastic
[docs-0.6.x-image]: http://img.shields.io/badge/docs-0.6.x-brightgreen.svg?style=plastic
[docs-0.5.x-image]: http://img.shields.io/badge/docs-0.5.x-brightgreen.svg?style=plastic

[rtd-devel-image]: https://readthedocs.org/projects/py-trees/badge/?version=devel&style=plastic
[rtd-1.2.x-image]: https://readthedocs.org/projects/py-trees/badge/?version=release-1.2.x&style=plastic
[rtd-0.6.x-image]: https://readthedocs.org/projects/py-trees/badge/?version=release-0.6.x&style=plastic
[rtd-0.5.x-image]: https://readthedocs.org/projects/py-trees/badge/?version=release-0.5.x&style=plastic
[not-available-docs-image]: http://img.shields.io/badge/docs-n/a-yellow.svg?style=plastic

[sources-devel]: https://github.com/splintered-reality/py_trees/tree/devel
[sources-1.2.x]: https://github.com/splintered-reality/py_trees/tree/release/1.2.x
[sources-0.6.x]: https://github.com/splintered-reality/py_trees/tree/release/0.6.x
[sources-0.5.x]: https://github.com/splintered-reality/py_trees/tree/release/0.5.x

[sources-devel-image]: http://img.shields.io/badge/sources-devel-blue.svg?style=plastic
[sources-1.2.x-image]: http://img.shields.io/badge/sources-1.2.x-blue.svg?style=plastic
[sources-0.6.x-image]: http://img.shields.io/badge/sources-0.6.x-blue.svg?style=plastic
[sources-0.5.x-image]: http://img.shields.io/badge/sources-0.5.x-blue.svg?style=plastic
