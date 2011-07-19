
from setuptools import setup

from events import VERSION

REQUIREMENTS = ('django',)
CLASSIFIERS = (
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
)

setup(
    name="django-events",
    version=VERSION,
    author='Aaron Madison',
    author_email='aaron.l.madison@gmail.com',
    description='A very basic events calendar app',
    packages=('events',),
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    zip_safe=False,
)