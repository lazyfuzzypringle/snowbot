#!/usr/bin/env python3

import os
import shutil
import click

import util
import cornell_data as cornell


@click.command()
@click.argument('dataset')
def cli(dataset):
    dataset = dataset.lower()
    if dataset == cornell.NAME:
        # TODO: maybe add a force remove folder
        dst = 'raw/cornell'
        if os.path.exists(dst):
            print('extracted cornell data already exist')
            return
        file = util.maybe_download(cornell.DATA_URL, download_dir='raw')
        util.maybe_extract(file, 'cornell-tmp')
        shutil.move('cornell-tmp/cornell movie-dialogs corpus', dst)
        shutil.rmtree('cornell-tmp', ignore_errors=True)
    else:
        print('unknown dataset', dataset)
    print('finish download and extract', dataset, 'dataset')


if __name__ == '__main__':
    cli()