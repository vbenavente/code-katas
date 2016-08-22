from setuptools import setup

setup(
    name="proper_parenthetics",
    description="A coding challenge",
    version=0.1,
    author="Victor Benavente",
    author_email="vbenavente@hotmail.com",
    license="MIT",
    py_modules=["proper_parenthetics"],
    package_dir={"": "src"},
    install_requires=[],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        "console_scripts": [
            "proper_parenthetics = proper_parenthetics:main"
        ]
    }
)
