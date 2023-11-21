import boto3
import re
import zlib

from colorhash import ColorHash
from django.conf import settings
from django.http import HttpResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SecondaryStructure(APIView):
    """SVG image for an RNA sequence"""

    def get_serializer(self, *args, **kwargs):
        return None

    @extend_schema(responses={(200, "image/svg"): OpenApiTypes.BINARY})
    def get(self, request, upi=None, format=None):
        s3 = boto3.resource(
            "s3",
            aws_access_key_id=settings.S3_SERVER["KEY"],
            aws_secret_access_key=settings.S3_SERVER["SECRET"],
            endpoint_url=settings.S3_SERVER["HOST"],
        )

        upi = list(self.kwargs["upi"])
        upi_path = (
            "".join(upi[0:3])
            + "/"
            + "".join(upi[3:5])
            + "/"
            + "".join(upi[5:7])
            + "/"
            + "".join(upi[7:9])
            + "/"
            + "".join(upi[9:11])
            + "/"
        )

        s3_file = "prod/" + upi_path + self.kwargs["upi"] + ".svg.gz"
        s3_obj = s3.Object(settings.S3_SERVER["BUCKET"], s3_file)
        try:
            s3_svg = zlib.decompress(s3_obj.get()["Body"].read(), zlib.MAX_WBITS | 32)
        except s3.meta.client.exceptions.NoSuchKey:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return HttpResponse(
            self.generate_thumbnail(s3_svg.decode("utf-8"), "".join(upi)),
            content_type="image/svg+xml",
        )

    def generate_thumbnail(self, image, upi):
        move_to_start_position = None
        color = ColorHash(upi).hex
        points = []
        width = []
        height = []

        for i, line in enumerate(image.split("\n")):
            if not width:
                width = re.findall(r'width="(\d+(\.\d+)?)"', line)
            if not height:
                height = re.findall(r'height="(\d+(\.\d+)?)"', line)
            for nt in re.finditer(
                '<text x="(\d+)(\.\d+)?" y="(\d+)(\.\d+)?".*?</text>', line
            ):
                if "numbering-label" in nt.group(0):
                    continue
                if not move_to_start_position:
                    move_to_start_position = "M{} {} ".format(nt.group(1), nt.group(3))
                points.append("L{} {}".format(nt.group(1), nt.group(3)))
        if len(points) < 200:
            stroke_width = "3"
        elif len(points) < 500:
            stroke_width = "4"
        elif len(points) < 3000:
            stroke_width = "4"
        else:
            stroke_width = "2"
        thumbnail = '<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}"><path style="stroke:{};stroke-width:{}px;fill:none;" d="'.format(
            width[0][0], height[0][0], color, stroke_width
        )
        thumbnail += move_to_start_position
        thumbnail += " ".join(points)
        thumbnail += '"/></svg>'
        return thumbnail
