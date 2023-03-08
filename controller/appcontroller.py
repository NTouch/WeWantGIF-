import json

from view.screen import Screen
from data import messages
from controller import helpers
from model.gif import Gif


class AppController:
    def __init__(self, output: Screen) -> object:
        """
        AppController object

        :param output: Screen to display info
        """
        self.output = output
        self.gifs = []

    def run_app(self):
        """
        handle query from users to get gif from GIPHY

        :return: None
        """
        self.output.show_message(messages.GREETING)

        # convert user's query characters in compatible url characters
        search = self.output.prompt_message(messages.SEARCH)
        search = helpers.format_for_url(search)

        number_of_result = self.number_of_result_input()

        # create url compatible with GIPHY API
        url = helpers.create_query_url(messages.URL_GIPHY, messages.API_KEY,
                                       search, number_of_result)

        # results of query in JSON
        url_response = helpers.http_request(url).json()

        self.create_gif(url_response["data"])

        helpers.put_gif_in_file(messages.HTML_PATH, self.gifs)

    def create_gif(self, gifs: dict) -> None:
        """
        instantiate Gif model for every gifs

        :param gifs: dict need ["id"],
                                ["title"],
                                ["url"],
                                (["height"], ["width"])
        :return: None
        """
        for gif in gifs:
            self.gifs.append(Gif(gif["id"], gif["title"], gif["url"], (gif["images"]["original"]["height"], gif["images"]["original"]["width"])))

    def number_of_result_input(self) -> str:
        """
        get an input from user and return it

        :return: str number of results wanted
        """
        while True:
            number_of_result = self.output.prompt_message(messages.NUMBER_OF_GIF)
            if helpers.is_valid_number(number_of_result):
                return number_of_result
            else:
                self.output.show_message("Il faut entrer un nombre...")
