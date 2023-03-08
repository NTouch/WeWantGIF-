class Gif:
    def __init__(self, id: str, title: str, url: str, size: list[str]):
        """
        Gif object base on GIPHY website gif

        :param id: str id from GIPHY
        :param title: str gif title
        :param url: str url of original gif
        :param size: list[str] (height, width) of gif
        """
        self.id =id
        self.title = title
        self.url = url
        self.size = size

    def __repr__(self):
        return f"{self.id} : {self.title}\n{self.url} // {self.size}"
