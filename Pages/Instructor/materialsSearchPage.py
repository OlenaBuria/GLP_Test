from Utils import env


class SearchMaterialsPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_for_materials_btn_id = "lookForMaterials"
        self.input_search_pearson_materials_text_field_id = "exchangeRedirect"
        self.select_course_list_link_text = env.CourseMaterial
        self.search_icon_css = ".pe-icon--search-lg-18"
        self.create_course_btn_css = ".pe-btn__cta--btn_xlarge"
        self.name_found_material_text_css = ".col-xs-9"

    def click_search_materials(self):
        self.driver.find_element_by_id(self.search_for_materials_btn_id).click()

    def input_pearson_materials(self, pearson_material):
        self.driver.find_element_by_id(self.input_search_pearson_materials_text_field_id).send_keys(pearson_material)

    def select_pearson_material(self):
        self.driver.find_element_by_link_text(self.select_course_list_link_text).click()

    def click_search_icon(self):
        self.driver.find_element_by_css_selector(self.search_icon_css).click()

    def click_create_course(self):
        self.driver.find_element_by_css_selector(self.create_course_btn_css).click()

    def name_found_material(self):  # page Create Course
        name_found_material = self.driver.find_element_by_css_selector(self.name_found_material_text_css).text
        return name_found_material




