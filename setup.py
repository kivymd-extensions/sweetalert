from setuptools import setup


if __name__ == "__main__":
    setup(
        extras_require={
            "docs": ["sphinx", "kivy", "sphinx-autoapi", "sphinx_rtd_theme"],
        },
        setup_requires=[],
        python_requires=">=3.6",
    )
