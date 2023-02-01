from distutils.core import setup

setup(
    name='ISCV',
    packages=['ISCV'],
    version='0.1.0',
    license='MIT',
    description='ISCV is an python library that lets you use machine learning models in an easy and productive way for your projects.',
    author='Mitansh Disha Meet Parnika',
    author_email='mitanshpanchal@gmail.com',
    url='https://github.com/looph0le/ISCV.git',
    keywords=['ComputerVision', 'HandTracking', 'FaceTracking', 'PoseEstimation'],
    install_requires=[
        'opencv-python',
        'mediapipe',
        'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
