from setuptools import setup

test_deps = ['pytest', 'Pillow', 'numpy']
extras = {
      "test": test_deps
}

setup(name='blurhash',
      version='1.1.3',
      description='Pure-Python implementation of the blurhash algorithm.',
      packages=['blurhash'],
      install_requires=[],
      tests_require=test_deps,
      extras_require=extras,
      url='https://github.com/halcy/blurhash-python',
      author='Lorenz Diener',
      author_email='lorenzd+blurhashpypi@gmail.com',
      license='No-Nazis',
      data_files = [("", ["LICENSE"])],
      keywords='blurhash graphics web_development',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Multimedia :: Graphics',
          'License :: Other/Proprietary License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ])
