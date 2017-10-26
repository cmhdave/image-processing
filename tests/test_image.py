import filecmp
import os
import shutil

from image_processing import format_converter, transform, validation
from test_utils import temporary_folder, filepaths, assert_lines_match


class TestImageFormatConverter:
    def test_converts_jpg_to_tiff(self):
        with temporary_folder() as output_folder:
            jpg_file = os.path.join(output_folder,'test.jpg')
            tiff_file = os.path.join(output_folder,'test.tif')
            shutil.copy(filepaths.VALID_JPG, jpg_file)

            format_converter.convert_to_tiff(jpg_file, tiff_file)
            assert os.path.isfile(tiff_file)


    def test_converts_jpg_to_tiff_image_magick(self):
        with temporary_folder() as output_folder:
            jpg_file = os.path.join(output_folder,'test.jpg')
            tiff_file = os.path.join(output_folder,'test.tif')
            shutil.copy(filepaths.VALID_JPG, jpg_file)

            format_converter.convert_to_tiff_with_library_choice(jpg_file, tiff_file, use_graphics_magick=False)
            assert os.path.isfile(tiff_file)


    # def test_converts_jpg_to_tiff_graphics_magick(self):
    #     with temporary_folder() as output_folder:
    #         jpg_file = os.path.join(output_folder,'test.jpg')
    #         tiff_file = os.path.join(output_folder,'test.tif')
    #         shutil.copy(filepaths.VALID_JPG, jpg_file)
    #
    #         format_converter.convert_to_tiff_with_library_choice(jpg_file, tiff_file, use_graphics_magick=True)
    #         assert os.path.isfile(tiff_file)

    def test_converts_jpg_to_jpeg2000(self):
        with temporary_folder() as output_folder:
            jpg_file = os.path.join(output_folder,'test.jpg')
            output_file = os.path.join(output_folder,'output.jp2')
            shutil.copy(filepaths.VALID_JPG, jpg_file)

            format_converter.convert_unsupported_file_to_jpeg2000(jpg_file, output_file)
            assert os.path.isfile(output_file)
            assert filecmp.cmp(output_file, filepaths.VALID_LOSSLESS_JP2)


class TestImageValidation:
    def test_verifies_valid_jpeg2000(self):
        assert validation.verify_jp2(filepaths.VALID_LOSSLESS_JP2)

    def test_verifies_valid_lossy_jpeg2000(self):
        assert validation.verify_jp2(filepaths.VALID_LOSSY_JP2)

    def test_recognises_invalid_jpeg2000(self):
        assert not validation.verify_jp2(filepaths.INVALID_JP2)


class TestImageTransform:
    def test_creates_correct_files(self):
        with temporary_folder() as output_folder:
            transform.transform_jpg_to_ingest_format(filepaths.VALID_JPG, output_folder)

            jpg_file = os.path.join(output_folder,'full.jpg')
            jp2_file = os.path.join(output_folder,'full_lossless.jp2')
            jp2_lossy_file = os.path.join(output_folder,'full_lossy.jp2')
            assert os.path.isfile(jpg_file)
            assert os.path.isfile(jp2_file)
            assert os.path.isfile(jp2_lossy_file)
            assert filecmp.cmp(jpg_file, filepaths.VALID_JPG)
            assert filecmp.cmp(jp2_file, filepaths.VALID_LOSSLESS_JP2)
            assert filecmp.cmp(jp2_lossy_file, filepaths.VALID_LOSSY_JP2)


    def test_does_not_generate_xmp(self):
        with temporary_folder() as output_folder:
            transform.transform_jpg_to_ingest_format(filepaths.VALID_JPG, output_folder, save_xmp=False)

            jpg_file = os.path.join(output_folder,'full.jpg')
            jp2_file = os.path.join(output_folder,'full_lossless.jp2')
            jp2_lossy_file = os.path.join(output_folder,'full_lossy.jp2')
            assert os.path.isfile(jpg_file)
            assert os.path.isfile(jp2_file)
            assert os.path.isfile(jp2_lossy_file)
            assert not os.path.isfile(os.path.join(output_folder,'xmp.xml'))
            assert filecmp.cmp(jpg_file, filepaths.VALID_JPG)
            assert filecmp.cmp(jp2_file, filepaths.VALID_LOSSLESS_JP2)

    def test_generates_xmp(self):
        with temporary_folder() as output_folder:
            transform.transform_jpg_to_ingest_format(filepaths.VALID_JPG, output_folder, save_xmp=True)

            jpg_file = os.path.join(output_folder, 'full.jpg')
            jp2_file = os.path.join(output_folder, 'full_lossless.jp2')
            xmp_file = os.path.join(output_folder, 'xmp.xml')

            assert os.path.isfile(jpg_file)
            assert os.path.isfile(jp2_file)
            assert os.path.isfile(xmp_file)

            assert filecmp.cmp(jpg_file, filepaths.VALID_JPG)
            assert filecmp.cmp(jp2_file, filepaths.VALID_LOSSLESS_JP2)
            assert_lines_match(xmp_file, filepaths.VALID_XMP)

    def test_bad_image_metadata_input(self):
        """"
        Tests that input images with invalid metadata can be valid once transformed. Transformed with metadata intact they create invalid jp2s
        """
        with temporary_folder() as output_folder:
            transform.transform_jpg_to_ingest_format(filepaths.BAD_METADATA_JPG, output_folder, strip_embedded_metadata=True)
