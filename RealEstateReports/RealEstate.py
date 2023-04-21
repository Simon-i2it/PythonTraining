import numpy
import pandas

from enum import Enum

from pandas import DataFrame
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4, A3


class Column(Enum):
    price = "price"
    location = "location"
    bedrooms = "bedrooms"
    bathrooms = "bathrooms"
    property_type = "property_type"
    square_footage = "square_footage"


class Margin(Enum):
    top = 50
    left = 50
    indentation = 20
    row_height = 30
    column_width = 150
    title_position = 550


class RealEstate:
    @staticmethod
    def read_csv_file(file_name: str) -> DataFrame:
        return pandas.read_csv(file_name)

    @staticmethod
    def get_average_price_square_footage_by_location(data_frame: DataFrame):
        return data_frame.groupby([Column.location.value]).agg(
            {
                Column.price.value: lambda x: f"Rs : {x.mean():.2f} Lakhs",
                Column.square_footage.value: lambda x: f"{x.mean():.2f} sq.ft",
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
                Column.square_footage.value: lambda x: f"{x.mean():.2f} sq.ft",
                Column.bedrooms.value: lambda x: numpy.round(x.mean()),
                Column.bathrooms.value: lambda x: numpy.round(x.mean()),
            }
        )

    @staticmethod
    def export_dataframe_to_pdf(file_name: str, title: str, data_frame: DataFrame, pagesize: tuple[float,float]):
        column_names = data_frame.index.names + list(data_frame.columns)
        column_values = [
            [row.name] + list(row.values) for _, row in data_frame.iterrows()
        ]

        pdf_file = canvas.Canvas(file_name, pagesize=landscape(pagesize))

        pdf_file.drawString(
            Margin.left.value,
            Margin.title_position.value,
            title,
        )

        for index, column_name in enumerate(column_names):
            pdf_file.drawString(
                Margin.left.value
                + Margin.indentation.value
                + index * Margin.column_width.value,
                Margin.title_position.value - Margin.row_height.value * 2,
                column_name,
            )

        for x, row in enumerate(column_values):
            for y, value in enumerate(row):
                pdf_file.drawString(
                    Margin.top.value
                    + Margin.indentation.value
                    + y * Margin.column_width.value,
                    Margin.title_position.value
                    - Margin.row_height.value * 2
                    - (x + 1) * Margin.row_height.value,  # + 1 for header
                    str(value),
                )

        pdf_file.save()

    # Execution

    data_frame = read_csv_file("RealEstateApp/PropertyData.csv")

    export_dataframe_to_pdf(
        f"RealEstateApp/{get_average_price_square_footage_by_location.__name__}.pdf",
        "Average Price and Square Footage of property in each Location :-",
        get_average_price_square_footage_by_location(data_frame), A4
    )

    export_dataframe_to_pdf(
        f"RealEstateApp/{get_average_rooms_by_property_type.__name__}.pdf",
        "Average Number of Bed and Bath rooms in a property for each property type :-",
        get_average_rooms_by_property_type(data_frame), A4
    )

    export_dataframe_to_pdf(
        f"RealEstateApp/{get_summary_by_location_property_type.__name__}.pdf",
        "Property's average Price, Square Footage, Number of Bed and Bath rooms in each property type and location :-",
        get_summary_by_location_property_type(data_frame), A3
    )
