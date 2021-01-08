from wagtail.core import blocks


"""
Blocks module entry point. Used to cleanly organize blocks into
individual files based on purpose, but provide them all as a
single `blocks` module.
"""

from django.utils.translation import gettext_lazy as _

from wagtail.core import blocks

from django.utils.translation import gettext_lazy as _

from coderedcms.blocks.stream_form_blocks import (
    CoderedStreamFormCharFieldBlock,
    CoderedStreamFormCheckboxesFieldBlock,
    CoderedStreamFormCheckboxFieldBlock,
    CoderedStreamFormDateFieldBlock,
    CoderedStreamFormDateTimeFieldBlock,
    CoderedStreamFormDropdownFieldBlock,
    CoderedStreamFormFileFieldBlock,
    CoderedStreamFormImageFieldBlock,
    CoderedStreamFormNumberFieldBlock,
    CoderedStreamFormRadioButtonsFieldBlock,
    CoderedStreamFormStepBlock,
    CoderedStreamFormTextFieldBlock,
    CoderedStreamFormTimeFieldBlock
)
from coderedcms.blocks.html_blocks import (
    ButtonBlock,
    EmbedGoogleMapBlock,
    ImageBlock,
    ImageLinkBlock,
    DownloadBlock,
    EmbedVideoBlock,
    PageListBlock,
    PagePreviewBlock,
    QuoteBlock,
    RichTextBlock,
    TableBlock
)
from coderedcms.blocks.content_blocks import (  # noqa
    CardBlock,
    CarouselBlock,
    ContentWallBlock,
    ImageGalleryBlock,
    ModalBlock,
    NavDocumentLinkWithSubLinkBlock,
    NavExternalLinkWithSubLinkBlock,
    NavPageLinkWithSubLinkBlock,
    PriceListBlock,
    ReusableContentBlock
)
from coderedcms.blocks.layout_blocks import (
    CardGridBlock,
    GridBlock,
    HeroBlock
)
from coderedcms.blocks.metadata_blocks import (  # noqa
    OpenHoursBlock,
    StructuredDataActionBlock
)
from coderedcms.blocks.base_blocks import (  # noqa
    BaseBlock,
    BaseLayoutBlock,
    BaseLinkBlock,
    ClassifierTermChooserBlock,
    CoderedAdvColumnSettings,
    CoderedAdvSettings,
    CoderedAdvTrackingSettings,
    CollectionChooserBlock,
    MultiSelectBlock
)


from wagtail.core.blocks import RawHTMLBlock


class MapBlock(blocks.StructBlock):
    """Main MapboxMap"""
    #title = blocks.CharBlock(required=True, help_text="Add your title")

   # cards = blocks.ListBlock(
    #    blocks.StructBlock([
     #       ]
    #)
    class Meta:
        template = "streams/map_block.html"
        icon ="placeholder"
        label = "Map Block"


# Collections of blocks commonly used together.

HTML_STREAMBLOCKS = [
    ('text', RichTextBlock(icon='fa-file-text-o')),
    ('button', ButtonBlock()),
    ('image', ImageBlock()),
    ('image_link', ImageLinkBlock()),
    ('html', RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'), )),
    ('download', DownloadBlock()),
    ('embed_video', EmbedVideoBlock()),
    ('quote', QuoteBlock()),
    ('table', TableBlock()),
    ('MapBox_map', MapBlock()),
    ('page_list', PageListBlock()),
    ('page_preview', PagePreviewBlock()),
]

CONTENT_STREAMBLOCKS = HTML_STREAMBLOCKS + [
    ('card', CardBlock()),
    ('carousel', CarouselBlock()),
    ('image_gallery', ImageGalleryBlock()),
    ('modal', ModalBlock(HTML_STREAMBLOCKS)),
    ('pricelist', PriceListBlock()),
    ('reusable_content', ReusableContentBlock()),
]

NAVIGATION_STREAMBLOCKS = [
    ('page_link', NavPageLinkWithSubLinkBlock()),
    ('external_link', NavExternalLinkWithSubLinkBlock()),
    ('document_link', NavDocumentLinkWithSubLinkBlock()),
]

BASIC_LAYOUT_STREAMBLOCKS = [
    ('row', GridBlock(HTML_STREAMBLOCKS)),
    ('html', RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'))),
]

LAYOUT_STREAMBLOCKS = [
    ('hero', HeroBlock([
        ('row', GridBlock(CONTENT_STREAMBLOCKS)),
        ('cardgrid', CardGridBlock([
            ('card', CardBlock()),
        ])),
        ('html', RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'))),
    ])),
    ('row', GridBlock(CONTENT_STREAMBLOCKS)),
    ('cardgrid', CardGridBlock([
        ('card', CardBlock()),
    ])),
    ('html', RawHTMLBlock(icon='code', classname='monospace', label=_('HTML'))),
]
"""
STREAMFORM_FIELDBLOCKS = [
    ('sf_singleline', CoderedStreamFormCharFieldBlock(group=_('Fields'))),
    ('sf_multiline', CoderedStreamFormTextFieldBlock(group=_('Fields'))),
    ('sf_number', CoderedStreamFormNumberFieldBlock(group=_('Fields'))),
    ('sf_checkboxes', CoderedStreamFormCheckboxesFieldBlock(group=_('Fields'))),
    ('sf_radios', CoderedStreamFormRadioButtonsFieldBlock(group=_('Fields'))),
    ('sf_dropdown', CoderedStreamFormDropdownFieldBlock(group=_('Fields'))),
    ('sf_checkbox', CoderedStreamFormCheckboxFieldBlock(group=_('Fields'))),
    ('sf_date', CoderedStreamFormDateFieldBlock(group=_('Fields'))),
    ('sf_time', CoderedStreamFormTimeFieldBlock(group=_('Fields'))),
    ('sf_datetime', CoderedStreamFormDateTimeFieldBlock(group=_('Fields'))),
    ('sf_image', CoderedStreamFormImageFieldBlock(group=_('Fields'))),
    ('sf_file', CoderedStreamFormFileFieldBlock(group=_('Fields'))),
]

STREAMFORM_BLOCKS = [
    ('step', CoderedStreamFormStepBlock(STREAMFORM_FIELDBLOCKS + HTML_STREAMBLOCKS)),
]

"""
