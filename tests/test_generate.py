import os

from da_forms.generate import write_to_file


def test_create_2404():
    output_dir = os.path.join('dist', 'DA2404_Sample.pdf')
    write_to_file(output_dir)
    assert os.path.exists(output_dir)
    print('Successfully created 2404 PDF')
