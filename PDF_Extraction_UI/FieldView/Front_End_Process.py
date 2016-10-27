


def restructure_pdf_name(original_file_name):
	file_name_str_list = original_file_name.split('_');
	new_pdf_file_name = ''.join([file_name_str_list[1],'.pdf']);
	return new_pdf_file_name;