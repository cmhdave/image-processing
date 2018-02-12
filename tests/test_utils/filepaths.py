

# adobe rgb 1998 8 bit tiff file (our most common input format) + expected derivatives
STANDARD_TIF = 'tests/data/standard_adobe.tif'
STANDARD_TIF_SINGLE_LAYER = 'tests/data/standard_adobe_tif_single_layer.tif'  # same tif but without thumbnail
LOSSY_JP2_FROM_STANDARD_TIF = 'tests/data/standard_adobe_tif_lossy.jp2'
LOSSLESS_JP2_FROM_STANDARD_TIF = 'tests/data/standard_adobe_tif.jp2'
RESIZED_JPG_FROM_STANDARD_TIF = 'tests/data/standard_adobe_tif_resized.jpg'
HIGH_QUALITY_JPG_FROM_STANDARD_TIF = 'tests/data/standard_adobe_tif_hq.jpg'
STANDARD_TIF_XMP = 'tests/data/standard_adobe_tif_xmp.xml'


# Monochrome tifs
GREYSCALE_TIF = 'tests/data/greyscale.tif'


BILEVEL_TIF = 'tests/data/bilevel.tif'
LOSSLESS_JP2_FROM_BILEVEL_TIF = 'tests/data/bilevel_tif.jp2'
RESIZED_JPG_FROM_BILEVEL_TIF = 'tests/data/bilevel_tif_resized.jpg'

GREYSCALE_NO_PROFILE_TIF = 'tests/data/greyscale_without_profile.tif'
RESIZED_JPG_FROM_GREYSCALE_NO_PROFILE_TIF = 'tests/data/greyscale_without_profile_tif_resized.jpg'
LOSSLESS_JP2_FROM_GREYSCALE_NO_PROFILE_TIF = 'tests/data/greyscale_without_profile_tif.jp2'

# adobe rgb 1998 8 bit jpg file (converted from tif) + expected derivatives
STANDARD_JPG = 'tests/data/standard_adobe.jpg'
TIF_FROM_STANDARD_JPG = 'tests/data/standard_adobe_jpg.tif'
LOSSLESS_JP2_FROM_STANDARD_JPG = 'tests/data/standard_adobe_jpg.jp2'
STANDARD_JPG_XMP = 'tests/data/standard_adobe_jpg_xmp.xml'

#misc tiffs
# for testing the pixel checksum
SMALL_TIF = 'tests/data/small.tif'
SMALL_TIF_WITH_CHANGED_PIXELS = 'tests/data/small_different_pixel.tif'
SMALL_TIF_WITH_CHANGED_METADATA = 'tests/data/small_different_metadata.tif'

NO_PROFILE_TIF = 'tests/data/no_profile.tif'

# just truncated files
INVALID_JP2 = 'tests/data/invalid.jp2'
INVALID_TIF = 'tests/data/invalid.tif'

KAKADU_BASE_PATH = '/opt/kakadu'
DEFAULT_IMAGE_MAGICK_PATH = '/usr/bin/'


