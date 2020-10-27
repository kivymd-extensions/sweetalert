if __name__ == "__main__":
    from setuptools import setup

    setup(
        extras_require={
            "docs":
                [
                    "sphinx",
                    "kivy",
                    "kivymd",
                    "sphinx-autoapi",
                    "sphinx_rtd_theme",
                    "future",
                    "pygments",
                    "yaml",
                ],
        },
        setup_requires=[],
        python_requires=">=3.6",
    )
