import pandas

from enum import Enum
from pandas import DataFrame
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib.pagesizes import landscape, A4


class Column(Enum):
    price = "Price"
    location = "Location"
    bedrooms = "Bedrooms"
    bathrooms = "Bathrooms"
    property_type = "PropertyType"
    area = "Area"


class RealEstate:
    @staticmethod
    def read_csv_file(file_name: str) -> DataFrame:
        return pandas.read_csv(file_name)

    @staticmethod
    def get_average_price_square_footage_by_location(data_frame: DataFrame):
        return data_frame.groupby([Column.location.value]).agg(
            {
                Column.price.value: lambda x: f"Rs : {x.mean():.2f} Lakhs",
                Column.area.value: lambda x: f"{x.mean():.2f} sq.ft",
            }
        )

    @staticmethod
    def get_average_rooms_by_property_type(data_frame: DataFrame):
        return (
            data_frame.groupby([Column.property_type.value])
            .agg({Column.bedrooms.value: "mean", Column.bathrooms.value: "mean"})
            .round(2)
        )

    @staticmethod
    def get_summary_by_location_property_type(data_frame: DataFrame):
        return data_frame.groupby(
            [Column.location.value, Column.property_type.value]
        ).agg(
            {
                Column.price.value: lambda x: f"Rs : {x.mean():.2f} Lakhs",
                Column.area.value: lambda x: f"{x.mean():.2f} sq.ft",
                Column.bedrooms.value: lambda x: x.mean(),
                Column.bathrooms.value: lambda x: x.mean(),
            }
        )

    @staticmethod
    def export_dataframe_to_pdf(
        title: str, data_frame: DataFrame, pagesize: tuple[float, float]
    ):
        pdf_row_px = 20
        pdf_margin_px = 80

        pdf_file = canvas.Canvas(
            f"RealEstateReports/{title}.pdf", pagesize, bottomup=100
        )
        pdf_file.drawString(
            pdf_margin_px, pagesize[1] - pdf_margin_px + 30, f"{title} :-"
        )

        data_frame = data_frame.reset_index()
        data = [list(data_frame)] + data_frame.values.tolist()

        table = Table(data)
        table_style = TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 1, colors.darkred),  # Table grid
                ("BACKGROUND", (0, 0), (-1, 0), colors.bisque),  # Header row
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.crimson),  # Header text color
                ("BACKGROUND", (0, 1), (-1, -1), colors.cornsilk),  # Data rows
                ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),  # Data text color
            ]
        )
        table.setStyle(table_style)

        table.wrapOn(pdf_file, 0, 0)
        table.drawOn(
            pdf_file,
            pdf_margin_px,
            pagesize[1] - pdf_row_px * data_frame.shape[0] - pdf_margin_px,
        )

        pdf_file.save()

    # Execution

    data_frame = read_csv_file("RealEstateReports/PropertyData.csv")
    replacements = {"get": "report", "_": " "}

    export_dataframe_to_pdf(
        "1. Average Price and Square Footage of property in each Location",
        get_average_price_square_footage_by_location(data_frame),
        landscape(A4),
    )

    export_dataframe_to_pdf(
        "2. Average Number of Bed and Bath rooms in a property for each property type",
        get_average_rooms_by_property_type(data_frame),
        landscape(A4),
    )

    export_dataframe_to_pdf(
        "3. Average Price, Square Footage, Number of Bed and Bath rooms in each property type and location",
        get_summary_by_location_property_type(data_frame),
        landscape(A4),
    )
