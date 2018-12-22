%define		plugin	tagbar
Summary:	Vim plugin: Display tags of the current file ordered by scope
Name:		vim-plugin-%{plugin}
Version:	2.7
Release:	1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	https://github.com/majutsushi/tagbar/archive/v%{version}.tar.gz
# Source0-md5:	aacb0d94f7d8e66afde9135c137cbae1
URL:		http://majutsushi.github.com/tagbar/
Requires:	ctags
Requires:	vim-rt >= 4:7.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Tagbar displays the tags of the current file in a sidebar. It has
the advantage that it will display them ordered by their scope -- for
example, methods and members in languages like C++, Python or Java
will be listed under their correct class instead of just under the
general categories 'functions' or 'variables'. This gives a more
helpful overview of the file.

Additionally the Tagbar window can be used to quickly jump to tags. 

%package doc
Summary:	Documentation for tagbar Vim plugin
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for tagbar Vim plugin.

%prep
%setup -qn %{plugin}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/
cp -pr autoload doc plugin $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc README.md
%{_vimdatadir}/autoload/tagbar.vim
%{_vimdatadir}/plugin/tagbar.vim

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/tagbar.txt
