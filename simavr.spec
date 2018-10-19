Name:    simavr
Version: 1.6
Release: 1%{?dist}
Summary: simavr - a lean and mean Atmel AVR simulator for linux
License: GPL-3.0
URL: https://github.com/buserror/simavr
BuildArch: noarch



%description
simavr is a new AVR simulator for linux, or any platform that uses avr-gcc. It uses avr-gcc's own register definition to simplify creating new targets for supported AVR devices. The core was made to be small and compact, and hackable so allow quick prototyping of an AVR project. The AVR core is now stable for use with parts with <= 128KB flash, and with preliminary support for the bigger parts. The simulator loads ELF files directly, and there is even a way to specify simulation parameters directly in the emulated code using an .elf section. You can also load multipart HEX files.

%prep
dnf install elfutils-libelf-devel gcc make avr-binutils avr-gcc avr-gdb avr-libc

%build
cd %{buildroot}
make all


%install
cd %{buildroot}
make install 

%files

%changelog
