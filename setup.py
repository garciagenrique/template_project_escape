import setuptools
import template_escape

setuptools.setup(name='template_project_escape',
                 version=template_escape.__version__,
                 description="Template project for the ESCAPE repository",
                 packages=setuptools.find_packages(),
                 install_requires=['numpy'],
                 package_data={'template_project_escape': ['./template_project_escape/*']},
                 tests_require=['pytest'],
                 author='https://github.com/garciagenrique',
                 author_email='garcia<at>lapp.in2p3.fr',
                 license='Open Source. MIT license. See LICENSE file.',
                 url='https://gitlab.in2p3.fr/escape2020/escape/template_project_escape'
                 )