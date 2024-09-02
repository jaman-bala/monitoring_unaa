from typing import Optional

from ninja import Schema


class CategorySchemas(Schema):
    id: int = None
    title: str = None
    slug: str = None

    class Config:
        from_attributes = True


class RegionSchemas(Schema):
    id: int = None
    title: str = None
    slug: str = None

    class Config:
        from_attributes = True


class CameraBase(Schema):
    category: CategorySchemas = None
    region: RegionSchemas = None
    id: int = None
    title: str = None
    url: str = None

    class Config:
        from_attributes = True


class CameraOutput(Schema):
    category: CategorySchemas = None
    region: RegionSchemas = None
    id: int = None
    title: str = None
    url: str = None
    status: str = None
    ping_status: Optional[int] = None

    class Config:
        from_attributes = True
