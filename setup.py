from setuptools import setup

setup(
  name='cesi',
  version='0.1.0-test-0',
  description='Centralized supervisor interface.',
  long_description=('uzun tanimlama'),
  url='http://github.com/GulsahKose/cesi',
  license='GPLv3',
  author='Gulsah Kose',
  author_email='gulsah.1004@gmail.com',
  install_requires=[
    "Flask>=0.10.1"
  ],
  include_package_data=True,
  packages=['pack'],
  package_dir={
    'pack': 'pack',
  },
  package_data={
    'pack' : [
      'static/*.js',
      'static/*.css',
      'static/*.png',
      'static/css/*.css',
      'static/css/plugins/dataTables/*.css',
      'static/css/plugins/morris/*.css',
      'static/css/plugins/social-buttons/*.css',
      'static/css/plugins/timeline/*.css',
      'static/font-awesome/css/*.css',
      'static/font-awesome/fonts/*.otf',
      'static/font-awesome/fonts/*.eot',
      'static/font-awesome/fonts/*.svg',
      'static/font-awesome/fonts/*.ttf',
      'static/font-awesome/fonts/*.woff',
      'static/font-awesome/less/*.less',
      'static/font-awesome/scss/*.scss',
      'static/fonts/*.eot',
      'static/fonts/*.svg',
      'static/fonts/*.ttf',
      'static/fonts/*.woff',
      'static/js/*.js',
      'static/js/demo/*.js',
      'static/js/plugins/dataTables/*.js',
      'static/js/plugins/flot/*.js',
      'static/js/plugins/metisMenu/*.js',
      'static/js/plugins/morris/*.js',
      'static/js/ui/jquery-ui-1.11.0/*.html',
      'static/js/ui/jquery-ui-1.11.0/*.js',
      'static/js/ui/jquery-ui-1.11.0/*.css',
      'static/js/ui/jquery-ui-1.11.0/external/jquery/*.js',
      'static/js/ui/jquery-ui-1.11.0/images/*.gif',
      'static/js/ui/jquery-ui-1.11.0/images/*.png',
      'static/js/ui/jquery-ui-1.11.0.custom/*.html',
      'static/js/ui/jquery-ui-1.11.0.custom/*.js',
      'static/js/ui/jquery-ui-1.11.0.custom/*.css',
      'static/js/ui/jquery-ui-1.11.0.custom/external/jquery/*.js',
      'static/js/ui/jquery-ui-1.11.0.custom/images/*.gif',
      'static/js/ui/jquery-ui-1.11.0.custom/images/*.png',
      'static/noty-2.2.4/*.json',
      'static/noty-2.2.4/*.js',
      'static/noty-2.2.4/*.txt',
      'static/noty-2.2.4/*.markdown',
      'static/noty-2.2.4/demo/*.html',
      'static/noty-2.2.4/demo/*.css',
      'static/noty-2.2.4/demo/*.js',
      'static/noty-2.2.4/js/noty/*.js',
      'static/noty-2.2.4/js/noty/layouts/*.js',
      'static/noty-2.2.4/js/noty/packaged/*.js',
      'static/noty-2.2.4/js/noty/themes/*.js',
      'templates/*.html'
   ]
  }
)
