from setuptools import setup, find_packages

setup(
    name="wtpsplit",
    version="2.1.4",
    packages=find_packages(),
    description="Universal Robust, Efficient and Adaptable Sentence Segmentation",
    author="Markus Frohmann, Igor Sterner, Benjamin Minixhofer",
    author_email="markus.frohmann@gmail.com",
    install_requires=[
        "onnxruntime>=1.13.1",
        "transformers>=4.22.2",
        "huggingface-hub",
        "numpy>=1.0",
        "scikit-learn>=1",
        "tqdm",
        "skops",
        "pandas>=1",
        "cached_property",  # for Py37
        "mosestokenizer",
    ],
    url="https://github.com/segment-any-text/wtpsplit",
    package_data={"wtpsplit": ["data/*"]},
    include_package_data=True,
    license="MIT",
)
