from setuptools import setup, find_packages

setup(
    name='latex_to_png',
    version='0.1.0',
    description='Render LaTeX code to PNG images with transparent background (no math mode required)',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'latexify=latex_to_png.cli:main',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
    zip_safe=False,
) 