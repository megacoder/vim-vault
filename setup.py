from setuptools import setup

setup(
    name = 'vim-vault',
    version = '0.0.0',
    description = 'Create and maintain a local copy of "vim-scripts".',
    long_description = 'More to follow, watch this space.',
    author = 'Tommy Reynolds',
    author_email = 'Oldest.Software.Guy@gmail.com',
    url = 'https://github.com/megacoder/vim-vault',
    keywords = ['vim-vault'],
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License'
    ],
    package_dir = {
        'vim-vault': 'src'
    },
    py_modules = [
        'vim-vault.__init__',
        'vim-vault.vim-vault'
    ]
)
