Name:           ros-melodic-py-trees
Version:        0.6.8
Release:        0%{?dist}
Summary:        ROS py_trees package

Group:          Development/Libraries
License:        BSD
URL:            http://py-trees.readthedocs.io
Source0:        %{name}-%{version}.tar.gz

Requires:       pydot
Requires:       python-enum34
BuildRequires:  python-setuptools
BuildRequires:  ros-melodic-catkin

%description
Pythonic implementation of behaviour trees.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Sun Feb 24 2019 Daniel Stonier <d.stonier@gmail.com> - 0.6.8-0
- Autogenerated by Bloom

* Sun Feb 24 2019 Daniel Stonier <d.stonier@gmail.com> - 0.6.7-1
- Autogenerated by Bloom

* Wed Feb 13 2019 Daniel Stonier <d.stonier@gmail.com> - 0.6.7-0
- Autogenerated by Bloom

* Tue Aug 21 2018 Daniel Stonier <d.stonier@gmail.com> - 0.6.1-0
- Autogenerated by Bloom

* Tue May 15 2018 Daniel Stonier <d.stonier@gmail.com> - 0.6.0-0
- Autogenerated by Bloom

