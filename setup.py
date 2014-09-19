from setuptools import setup

setup(
    name="tgit",
    version='0.1.1',
    author='Jason Liu',
    author_email='jx5liu@uwaterloo.ca',
    url="http://jxnl.co",
    packages=['tgit'],
    scripts=['tgit/tgit'],
    license='LICENSE.txt',
    description="""Tweet Those Commits""",
    long_description=open("README.md").read(),
    install_requires=['envoy', 'twitter', 'argparse'],
)
