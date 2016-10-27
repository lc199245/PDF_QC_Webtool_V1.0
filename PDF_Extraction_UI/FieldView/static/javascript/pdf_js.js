


function ajax_highlight(field_value_id){

								document.getElementById(field_value_id+"_btn").disabled = true;

								document.getElementById('highlight_image').style.opacity=0.1;
								var temp = document.getElementsByClassName("info info_border");
								if (temp.length !=0){
									temp_1 = temp[0]
									// alert(temp_1.textContent);
									document.getElementsByClassName("info")[0].className="";
								}
								document.getElementById(field_value_id).className = "info info_border";


								document.getElementById("highlight_detail_1").innerHTML = field_value_id;
								document.getElementById("highlight_detail_2").innerHTML = document.getElementById(field_value_id+"_cu").innerHTML;
								document.getElementById("highlight_detail_3").innerHTML = document.getElementById(field_value_id+"_tc").innerHTML;
								document.getElementById("highlight_detail_4").innerHTML = document.getElementById(field_value_id+"_ci").innerHTML;
								document.getElementById("highlight_detail_5").innerHTML = document.getElementById(field_value_id+"_fv").innerHTML;
								document.getElementById("highlight_detail_6").innerHTML = document.getElementById(field_value_id+"_cv").innerHTML;
								document.getElementById("highlight_detail_7").innerHTML = document.getElementById(field_value_id+"_cvsd").innerHTML;
								document.getElementById("highlight_detail_8").innerHTML = document.getElementById(field_value_id+"_cf").innerHTML;
								
								$.ajax({
								    type:'GET',
								    url:"/FieldView/" + field_value_id +  "/ajax_highlight",

								    dataType:'json',
								    success:function(data)
								        {
								            // alert(data[0].binpic);
								            document.getElementById(field_value_id+'_btn').disabled = false;
								            document.getElementById(field_value_id+'_btn').textContent = "";
								            document.getElementById('highlight_image').style.opacity=1;
								            document.getElementById('highlight_image').src = "data:image/jpeg;base64,"+data[0].binpic;
								            document.getElementById('highlight_image').style = "max-width:100%; max-height:100%;";
								            document.getElementById('highlight_image_2').src = "data:image/jpeg;base64,"+data[0].binpic;
								            document.getElementById('highlight_image_2').style = "max-width:100%; max-height:100%;";
								            document.getElementById('ajax_text').InnerHTML = data.binpic;

								        },
								    error:function(data)
								    {
								        alert("Operate too frequently, server crashed."); 
								    }
								});
								// document.getElementById('120425_btn').disabled = false;
							};


function highlight_dialog(){
		$(".modal-wide").on("show.bs.modal", function() {
		  var height = $(window).height() - 200;
		  $(this).find(".modal-body").css("max-height", height);
		});
};


function edit_dialog(field_value_id){
		ajax_highlight(field_value_id);
		$(".modal-wide").on("show.bs.modal", function() {
		  var height = $(window).height() - 200;
		  $(this).find(".modal-body").css("max-height", height);
		});
};


function show_calcrt_id(field_value_id){
	calcrt_id_list = document.getElementById("calcrtpicker");

	var calcrt_id = document.getElementById(field_value_id+'_ci').innerHTML.trim();

	for (i=0; i < calcrt_id_list.options.length; i++){
		if (calcrt_id == calcrt_id_list.options[i].value){
			document.getElementById(field_value_id+'_ci').title = calcrt_id_list.options[i].text;
		}
	}

};



function false_field(field_value_id){

	var temp = document.getElementsByClassName("info info_border");
	if (temp.length !=0){
	temp_1 = temp[0]
		// alert(temp_1.textContent);
		document.getElementsByClassName("info")[0].className="";
	}
	document.getElementById(field_value_id).className = "info info_border";
};

global_field_value_id = 0;
global_check_flag = 0;

temp_fix_or_false_row_id = 0;
temp_fix_or_false_row_classname = 0;

function focus_on_row(field_value_id){
	// alert('haha');
	if (document.getElementById(field_value_id+"_check_box").checked){
		document.getElementById(field_value_id).className = "warning";
	}else{
		document.getElementById(field_value_id).className = "";
	}

};


// function fix_field(){

// 	document.getElementById(global_field_value_id+"_btn_edit").textContent="Proccessing...";
// 	document.getElementById(global_field_value_id+"_btn_edit").disabled = true;
// };


// function false_field(){
// 	document.getElementById(global_field_value_id+"_btn_edit").textContent="Proccessing...";
// 	document.getElementById(global_field_value_id+"_btn_edit").disabled = true;	
// };


function reset_css(){
	// alert(global_field_value_id);
	reset_all_fix();
	reset_all_false();
	document.getElementById(global_field_value_id+"_btn_edit").textContent = "Unprocessed";
	document.getElementById(global_field_value_id+"_btn_edit").disabled = false;
};


function reset_all_fix(){
	$("#fix_comment_textarea").val("");
};



function reset_all_false(){
	$("#false_comment_textarea").val("");
};


function fix_field_submit(){
	for (i = 0; i<selected_id_cf_pairs.length; i++){	
		// alert(selected_id_cf_pairs[i]);	
		field_value_id = selected_id_cf_pairs[i][0];
		check_flag = selected_id_cf_pairs[i][1];
		var comments = document.getElementById("fix_comment_textarea").value;
		var calcrt_value = document.getElementById(field_value_id+'_cv').innerHTML;
		// alert(comments);
		// alert(global_check_flag);
		// alert(static_number_of_items);
		static_number_of_items = static_number_of_items - 1;
		// comments = remove_special_char(comments);
		// alert(comments);
		// alert(doc_id);

		$.ajax({
		    type:'GET',
		    url:"/FieldView/" + field_value_id +  "/fix_field",
		    dataType:'json',
		   	data: {'field_value_id': field_value_id, 'check_flag': check_flag, 'comments': comments, 'calcrt_value': calcrt_value, 'number_of_items': static_number_of_items},
		    success:function(data)
		        {
		            // alert(data[0].binpic);
		            // $('#FixModal').modal('hide');
		            // alert(field_value_id);
		   //          document.getElementById(field_value_id).disabled = true;
		   //          // document.getElementById(field_value_id+"_btn_edit").textContent="Fixed";
	    // 			document.getElementById(field_value_id).className="success";
					// // document.getElementById(field_value_id+"_btn_edit").disabled = true;
		        },
		    error:function(data)
		    {
		        alert("User error."); 
		        static_number_of_items = static_number_of_items + 1;
		    }
		});
		document.getElementById(field_value_id+"_btn").disabled = true;
		document.getElementById(field_value_id+"_check_box").disabled = true;
		document.getElementById(field_value_id+"_check_box").checked = false;
		document.getElementById(field_value_id+"_check_box_text").innerHTML = "Fixed";
		// document.getElementById(field_value_id+"_btn_edit").textContent="Fixed";
	    document.getElementById(field_value_id).className="success";
	}
	selected_id_cf_pairs = [];
	document.getElementById("fix_comment_textarea").value="";

};


function false_field_submit(){
	for (i=0; i<selected_id_cf_pairs.length; i++){
		field_value_id = selected_id_cf_pairs[i][0];
		check_flag = selected_id_cf_pairs[i][1];

		var error_picker = document.getElementById("error_picker").value;

		var comments = document.getElementById("false_comment_textarea").value;


		if (error_picker=='1'){
			comments = "The extraction value is wrong.  " + comments;
		}	

		if (error_picker=='2'){
			comments = "The api value is wrong.  " + comments;
		}	

		if (!comments.trim()){
			alert("Please type in a comment.");
			reset_css();
			return;
		}


		var calcrt_value = document.getElementById(field_value_id+'_cv').innerHTML;

		static_number_of_items = static_number_of_items - 1;
		$.ajax({
		    type:'GET',
		    url:"/FieldView/" + field_value_id +  "/false_field",
		    dataType:'json',
		   	data: {'field_value_id': field_value_id, 'check_flag': check_flag, 'comments': comments, 'calcrt_value': calcrt_value, 'number_of_items': static_number_of_items},
		    success:function(data)
		        {

		        },
		    error:function(data)
		    {
		        alert("User error."); 
		        static_number_of_items = static_number_of_items + 1;
		    }
		});
		document.getElementById(field_value_id+"_btn").disabled = true;
		document.getElementById(field_value_id+"_check_box").disabled = true;
		document.getElementById(field_value_id+"_check_box").checked = false;
		document.getElementById(field_value_id+"_check_box_text").innerHTML = "False";
	    document.getElementById(field_value_id).className="danger";

	
	}

	document.getElementById("false_comment_textarea").value="";
	document.getElementById("error_picker").value='0';

};



function file_lockup_check(doc_id){
	// alert(doc_id);
	$.ajax({
	    type:'GET',
	    url:"/FieldView/" + doc_id +  "/check_availability",
	    dataType:'json',
	   	data: {'doc_id': doc_id},
	    success:function(data)
	        {
	        },
	    error:function(data)
	    {
	        alert("This document is currently under QC by another analyst."); 
	    }
	});
};



function release_file(doc_id){
	$.ajax({
	    type:'GET',
	    url:"/FieldView/release_file",
	    dataType:'json',
	   	data: {'doc_id': doc_id, 'number_of_items': static_number_of_items},
	    success:function(data)
	        {
	            // alert(data[0].binpic);
	            // $('#FixModal').modal('hide');

	        },
	    error:function(data)
	    {
	        alert("User error"); 
	    }
	});	

};


function handle_close(doc_id){
	release_file(doc_id)
};


function direct_terminal(field_value_id){
	if (temp_fix_or_false_row_id !== 0 && field_value_id !== temp_fix_or_false_row_id){
		document.getElementById(temp_fix_or_false_row_id).className = temp_fix_or_false_row_classname;
	}

	global_check_flag = document.getElementById(field_value_id+"_check_flag").innerHTML;
	// alert(global_check_flag);
	global_field_value_id = field_value_id;

	if (document.getElementById(field_value_id).className=='success' || document.getElementById(field_value_id).className=='danger' || document.getElementById(field_value_id).className=='warning'){
		temp_fix_or_false_row_id = field_value_id;
		temp_fix_or_false_row_classname = document.getElementById(field_value_id).className;	
	}

	var temp = document.getElementsByClassName("info info_border");
	if (temp.length !=0){
	temp_1 = temp[0]
		// alert(temp_1.textContent);
		document.getElementsByClassName("info")[0].className="";
	}
	document.getElementById(field_value_id).className = "info info_border";
	document.getElementById(field_value_id+"_click").click();
};



function onload_func(){
	// alert('loaded!');
	
	
};



var selected_id_cf_pairs = [];

function bulk_fix(){
	var cb_list = document.getElementsByClassName("selected_check_box");
	selected_id_cf_pairs = [];
	for (var i=0; i<cb_list.length; i++){
		if (cb_list[i].checked){
			var id_string = cb_list[i].id;
			// alert(id_string);
			// alert(id_string.substring(0,id_string.indexOf('_')));
			var id_number = id_string.substring(0,id_string.indexOf('_'));
			// alert(document.getElementById(id_number+'_check_flag').innerHTML);
			var check_flag = document.getElementById(id_number+'_check_flag').innerHTML;
			var field_type = document.getElementById(id_number+'_ci').innerHTML;
			selected_id_cf_pairs.push([id_number,check_flag, field_type]);
			// fix_field_submit(id_number, check_flag);
		}
	}

	if (selected_id_cf_pairs.length > 100){
		alert("Number of selected errors is greater than 100, database access rejected.");
		bulk_clear();
		return false;
	}



	if (selected_id_cf_pairs.length==0){
		alert("Please select an error.");
		return false;
	}else{
		show_initial_info_on_modal();
		$('#FixModal').modal('show');
		// alert(selected_id_cf_pairs.length);
	}	
};



function bulk_false(){
	var cb_list = document.getElementsByClassName("selected_check_box");
	selected_id_cf_pairs = [];
	for (var i=0; i<cb_list.length; i++){
		if (cb_list[i].checked){
			var id_string = cb_list[i].id;
			// alert(id_string);
			// alert(id_string.substring(0,id_string.indexOf('_')));
			var id_number = id_string.substring(0,id_string.indexOf('_'));
			// alert(document.getElementById(id_number+'_check_flag').innerHTML);
			var check_flag = document.getElementById(id_number+'_check_flag').innerHTML;
			var field_type = document.getElementById(id_number+'_ci').innerHTML;
			selected_id_cf_pairs.push([id_number,check_flag, field_type]);
			// fix_field_submit(id_number, check_flag);
		}
	}
	// alert(cb_list.length);
	if (selected_id_cf_pairs.length > 100){
		alert("Number of selected errors is greater than 100, database access rejected.");
		bulk_clear();
		return false;
	}



	if (selected_id_cf_pairs.length==0){
		alert("Please select an error.");
		return false;
	}else{
		show_initial_info_on_modal_2();
		$('#EditModal').modal('show');
		// alert(selected_id_cf_pairs.length);
	}	

};


function bulk_clear(){
	var cb_list = document.getElementsByClassName("selected_check_box");

	for (var i=0; i<cb_list.length; i++){
		if (cb_list[i].checked){
			cb_list[i].checked = false;
			var id_string = cb_list[i].id;
			var id_number = id_string.substring(0,id_string.indexOf('_'));
			document.getElementById(id_number).className = "";	
		}	
	}	


};

function show_initial_info_on_modal_2(){
	// alert('hehe');
	document.getElementById("des_modal_number_2").innerHTML = "Number of errors selected: " + selected_id_cf_pairs.length;
    var temp_field_list = [];
	for (i=0;i<selected_id_cf_pairs.length;i++){
		temp_field_list.push(selected_id_cf_pairs[i][2]);
	}
	var temp_unique_field_list = [];
	$.each(temp_field_list, function(i, el){
    	if($.inArray(el, temp_unique_field_list) === -1) temp_unique_field_list.push(el);
	});
	document.getElementById("des_modal_fields_2").innerHTML = "Fields including: " + temp_unique_field_list;
};



function show_initial_info_on_modal(){
	// alert('hehe');
	document.getElementById("des_modal_number").innerHTML = "Number of errors selected: " + selected_id_cf_pairs.length;
    var temp_field_list = [];
	for (i=0;i<selected_id_cf_pairs.length;i++){
		temp_field_list.push(selected_id_cf_pairs[i][2]);
	}
	var temp_unique_field_list = [];
	$.each(temp_field_list, function(i, el){
    	if($.inArray(el, temp_unique_field_list) === -1) temp_unique_field_list.push(el);
	});
	document.getElementById("des_modal_fields").innerHTML = "Fields including: " + temp_unique_field_list;
};


function bulk_check(){
	var visible_rows = $('tr').filter(function() {
  	return $(this).css('display') !== 'none';
	});


	for (i=0;i<visible_rows.length;i++){
		// alert(num_of_visible_rows[2].id);
		if (!((visible_rows[i].id) == '')){
			// alert(visible_rows[i].id);
			document.getElementById(visible_rows[i].id+"_check_box").checked = true;
			document.getElementById(visible_rows[i].id).className = 'warning';
		}
	}	
};