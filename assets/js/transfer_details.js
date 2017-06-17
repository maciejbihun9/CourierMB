var package_details;

var $_address_section;
var $_packages_section;
var $_selected_package_section;
var $_duty_section;
var $_payment_section;
var $_confirmation_section;

var $_selected_package_size;

$(document).ready(function() {

    //init calendar


    package_details = {
      "SMALL": {
        size : "15,24 cm x 15,24 cm x 96,52 cm",
        max_weight : "5kg"
      },
      "MEDIUM" : {
        size : "29,21 cm x 6,03 cm x 33,66 cm",
        max_weight : "10kg"
      },
      "LARGE" : {
        size: "35 cm x 10 cm x 45 cm",
        max_weight: "15kg"
      }
    };

    $_address_section = $('#addressSection');
    $_packages_section = $('#packageTypeSection');
    $_selected_package_section = $('#selectedPackageTypeSection');
    $_duty_section = $('#dutySection');
    $_payment_section = $('#paymentSection');
    $_confirmation_section = $('#confirmationSection');
    $_selected_package_size = $('#packageSize');

    //price section
    $_price_label = $('#price_label');
    $_pack_weight_input = $('#pack_weight_input');
    $_pack_post_airport_select= $('#post_airport_select');
    $_pack_dest_airport_select = $('#dest_airport_select');
    $_pack_contents_input = $('#pack_contents_input');
});



function handle_package_type(img_name, element_name){
    //var new_content = generate_package_details_html(img_name);
    //$( "#packages_area" ).replaceWith( new_content );
    var $_packages_area = $('#packageTypeSection');
    var $_selected_package_type = $('#selectedPackageTypeSection');
    if ($_packages_area.css("display") == 'none'){
        $_packages_area.css("display", "unset");
        $_selected_package_type.css("display", "none");
        $_duty_section.css("display", "none");
    } else if($_packages_area.css("display") != 'none') {
        $_packages_area.css("display", "none");
        $_duty_section.css("display", "none");
        $_selected_package_type.css("display", "unset");
        selected_package_type = element_name;
        set_package_size_label(element_name);
        var image_url = '../../static/images/' + img_name;
        $("#selectedPkg").attr("src", image_url);
        set_package_size_label(element_name);
    }
}

function set_package_size_label(el_name){
    var package_size = $("#packageSize");
    if (el_name == "SMALL"){
        package_size.html(package_details.SMALL.size);
    } else if(el_name == "MEDIUM"){
        package_size.html(package_details.MEDIUM.size);
    } else if(el_name == "LARGE"){
        package_size.html(package_details.LARGE.size);
    }
}

function show_package_type_section(){
    show_element($_packages_section);
}

/* SHOW VIEWS FUNCTIONS */
function show_duty_section(){
    show_element($_duty_section);
}

function show_payment_section(){
    show_element($_payment_section);
}

function show_conf_section(){
    show_element($_confirmation_section);
}

function show_element($_element){
    $_address_section.css("display", "none");
    $_packages_section.css("display", "none");
    $_selected_package_section.css("display", "none");
    $_duty_section.css("display", "none");
    $_payment_section.css("display", "none");
    $_confirmation_section.css("display", "none");
    $_element.css("display", "unset");
}

function go_to_previous_page(element){
    console.log('works?');
    var previousPageId = element.parentNode.parentNode.parentNode.previousElementSibling.children[1].id;
    debugger;
    show_element($("#" + previousPageId));
}

function save_package(){
    pack_weight = $_pack_weight_input.val();
    post_airport_input_value = $_pack_post_airport_select.val();
    dest_airport_input_value = $_pack_dest_airport_select.val();
    pack_contents_input_value = $_pack_contents_input.val();
    var url = '/courierMB/actions/save_package/';
    var package = { weight: pack_weight, post_air_port: post_airport_input_value,
                    dest_air_port: dest_airport_input_value, contents: pack_contents_input_value,
                    package_type: selected_package_type};
    request("POST", url, package)
}

var dest_airport_lat = 0;
var dest_airport_long = 0;
var post_airport_lat = 0;
var post_airport_long = 0;

function on_change_dest(){
    dest_airport_select_value = $_pack_dest_airport_select.val();
    console.log(dest_airport_select_value);
    var url = '/courierMB/actions/get_airport/';
    var airport_name = {name: dest_airport_select_value, name2 : dest_airport_select_value};
    request("POST", url, airport_name, set_dest_airport_coordinates);
}

function on_change_post(){
    post_airport_select_value = $_pack_post_airport_select.val();
    var url = '/courierMB/actions/get_airport/';
    var airport_name = {name: post_airport_select_value, name2 : post_airport_select_value};
    console.log(post_airport_select_value);
    request("POST", url, airport_name, set_post_airport_coordinates);
}

function set_post_airport_coordinates(data){
    post_airport_lat = parseFloat(data.latitude);
    post_airport_long = parseFloat(data.longitude);
}

function set_dest_airport_coordinates(data){
    dest_airport_lat = parseFloat(data.latitude);
    dest_airport_long = parseFloat(data.longitude);
}

function compute_distance(){
    return getDistanceFromLatLonInKm(dest_airport_lat, dest_airport_long, post_airport_lat, post_airport_long);
}

function check_price(){
    //params = [11.24237542, -0.02394846]
    var weight = Math.round($_pack_weight_input.val());
    var distance = Math.round(compute_distance());
    var price = 11.24 * parseFloat(distance) + 2.39 * parseFloat(weight);
    $_price_label.text(Math.round(price / 100) + " " + "€");
}