var package_details = {
  tube: {
    "size" : "15,24 cm x 15,24 cm x 96,52 cm",
    "max_weight" : "10kg"
  },
  box : {
    "size" : "29,21 cm x 6,03 cm x 33,66 cm",
    "max_weight" : "15kg"
  },
  pack : {
    "size" : "30,48 cm x 39,37 cm ",
    "mx_weight" : "20kg"
  },
  envelope : {
    "size": "24,13 cm x 39,37 cm ",
    "max_weight" : "25kg"
  }
};

var $_packages_area = $('#packages_area');
var $_selected_package_type = $('#selected_package_type');
var $_duty_info = $('#duty_info');
var $_payment_area = $('#payment_area');
var $_confirmation_area = $('#confirmation_area');


function package_page_redirect(pkg_types_disp, pkg_type_disp){
    $_packages_area.css("display", pkg_types_disp);
    $_selected_package_type.css("display", pkg_type_disp);
    console.log("redirect works!!!");
}

function go_to_pkg_type(img_name, element_name){
    var x = document.getElementById("selected_package_type").previousSibling;
    var $_packages_area = $('#packages_area');
    var nextElementSiblingId = $_packages_area[0].nextElementSibling.id;
    console.log("first item : " + $_packages_area[0]);
    debugger;
    var $_selected_package_type = $('#selected_package_type');
    var image_url = '../../static/images/' + img_name;
    $("#selected_pkg").attr("src", image_url);
    set_package_size_label(element_name);
    package_page_redirect("none", "unset", "none");
}

function handle_package_page(img_name, element_name){
    //var new_content = generate_package_details_html(img_name);
    //$( "#packages_area" ).replaceWith( new_content );
    var $_packages_area = $('#packages_area');
    var $_selected_package_type = $('#selected_package_type');
    if ($_packages_area.css("display") == 'none'){
        $_packages_area.css("display", "unset");
        $_selected_package_type.css("display", "none");
        $_duty_info.css("display", "none");
    } else if($_packages_area.css("display") != 'none') {
        $_packages_area.css("display", "none");
        $_duty_info.css("display", "none");
        $_selected_package_type.css("display", "unset");
        var image_url = '../../static/images/' + img_name;
        $("#selected_pkg").attr("src", image_url);
        set_package_size_label(element_name);
    }
}

function set_package_size_label(el_name){
    var package_size = $("#package_size");
    if (el_name == "pack"){
        package_size.html(package_details.pack.size);
    } else if(el_name == "tube"){
        package_size.html(package_details.tube.size);
    } else if(el_name == "envelope"){
        package_size.html(package_details.envelope.size);
    } else {
        package_size.html(package_details.box.size);
    }
}

/* SHOW VIEWS FUNCTIONS */
function show_duty_area(){
    var $_duty_info = $('#duty_info');
    show_element($_duty_info);
}

function show_payment_area(){
    var $_payment_area = $('#payment_area');
    show_element($_payment_area);
}

function show_conf_area(){
    var $_confirmation_area = $('#confirmation_area');
    show_element($_confirmation_area);
}

function show_element($_element){
    var $_packages_area = $('#packages_area');
    var $_selected_package_type = $('#selected_package_type');
    var $_duty_info = $('#duty_info');
    var $_payment_area = $('#payment_area');
    var $_confirmation_area = $('#confirmation_area');
    $_packages_area.css("display", "none");
    $_selected_package_type.css("display", "none");
    $_duty_info.css("display", "none");
    $_payment_area.css("display", "none");
    $_confirmation_area.css("display", "none");
    $_element.css("display", "unset");
}

function go_to_previous_page(element){
    var previousPageId = element.parentNode.parentNode.previousElementSibling.id;
    show_element($("#" + previousPageId));
}