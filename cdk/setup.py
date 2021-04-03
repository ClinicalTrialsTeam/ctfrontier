from setuptools import setup

setup(
    name="ctf",
    version="0.1",
    py_modules=["ctf"],
    install_requires=[
        "Click",
    ],
    entry_points="""
        [console_scripts]
        ctf=ctf:cli
    """,
)
