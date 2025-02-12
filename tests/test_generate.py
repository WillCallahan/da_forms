import os

from da2404.generate import write_to_file


def test_create_2404():
    output_dir = os.path.join(os.path.pardir, 'dist', 'DA2404_Sample.pdf')
    write_to_file(output_dir)
    assert os.path.exists(output_dir)
    print('Successfully created 2404 PDF')


