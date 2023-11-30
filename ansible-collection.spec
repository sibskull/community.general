Name:    ansible-collection
Version: 8.0.2
Release: alt1

Summary: This repository contains the community.general Ansible Collection
License: GPL-3.0+ and Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT and MPL-2.0 and PSF-2.0
Group:   Development/Python3
URL:     https://github.com/ansible-collections/community.general

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source: %name-%version.tar

%description
This repository contains the community.general Ansible Collection. The
collection is a part of the Ansible package and includes many modules and
plugins supported by Ansible community which are not part of more specialized
community collections.

%package -n ansible
Summary: Curated set of Ansible collections included in addition to ansible-core
Group: System/Configuration/Other
License: GPL-3.0+ and Apache-2.0 and BSD-2-Clause and BSD-3-Clause and MIT and MPL-2.0 and PSF-2.0
Requires: ansible-core
Requires: %name = %EVR

%description -n ansible
Ansible is a radically simple model-driven configuration management,
multi-node deployment, and remote task execution system. Ansible works
over SSH and does not require any software or daemons to be installed
on remote nodes. Extension modules can be written in any language and
are transferred to managed machines automatically.

This package provides a curated set of Ansible collections included in addition
to ansible-core

%prep
%setup -n %name-%version
# Remove modules moved to ansible-core
rm -f plugins/modules/apt_{rpm,repo}.py

%install
mkdir -p %buildroot%python3_sitelibdir/ansible
cp -a plugins/* %buildroot%python3_sitelibdir/ansible

%files
%doc README.md CHANGELOG.rst
%python3_sitelibdir/ansible/*

%files -n ansible

%changelog
* Tue Nov 14 2023 Andrey Cherepanov <cas@altlinux.org> 8.0.2-alt1
- Initial build for Sisyphus.
