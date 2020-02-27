from collections import Sequence

from django.forms import ImageField


class DmitryImageField(ImageField):

    def __init__(self, *args, valid_types:Sequence[str]=(), **kwargs):
        ImageField.__init__(self, *args, **kwargs)

    def to_python(self, data):
        f = super(DmitryImageField, self).to_python(data)
        if f is None:
            return None

        try:
            from PIL import Image
        except ImportError:
            import Image

        # We need to get a file object for PIL. We might have a path or we might
        # have to read the data into memory.
        if hasattr(data, 'temporary_file_path'):
            file = data.temporary_file_path()
        else:
            if hasattr(data, 'read'):
                file = BytesIO(data.read())
            else:
                file = BytesIO(data['content'])

        try:
            im = Image.open(file)
            if im.format not in ('BMP', 'PNG', 'JPEG'):
                raise ValidationError("Unsupport image type. Please upload bmp, png or jpeg")
        except ImportError:
            # Under PyPy, it is possible to import PIL. However, the underlying
            # _imaging C module isn't available, so an ImportError will be
            # raised. Catch and re-raise.
            raise
        except Exception: # Python Imaging Library doesn't recognize it as an image
            raise ValidationError(self.error_messages['invalid_image'])