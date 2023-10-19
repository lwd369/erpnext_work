from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_wxwork/__init__.py
from erpnext_wxwork import __version__ as version

setup(
	name="erpnext_wxwork",
	version=version,
	description="mixin weixin work",
	author="zhuguoqing",
	author_email="317260164@qq.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
