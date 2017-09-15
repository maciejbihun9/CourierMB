$(document).ready(function() {

    // init admin panel objects
    $_admin_panel_price_for_tour = $('#admin_panel_price_for_tour');
    $_admin_panel_total_earnings = $('#admin_panel_total_earnings');
    $_admin_panel_earnings_from_packages = $('#admin_panel_earnings_from_packages');
    $_admin_panel_trip_order = $('#admin_panel_trip_order');
    $_admin_panel_add_packages_input = $('#admin_panel_add_packages_input');
    $_admin_panel_packages_status = $('#admin_panel_packages_status');
    $_admin_panel_remove_packages_input = $('#admin_panel_remove_packages_input');
});

//run courierMB simulated annealing algorithm
function run_algorithm(){
    // use ajax to run algorithm
    if (parseInt($_admin_panel_packages_status.text()) < 500){
        alert("There is not enough packages. There is high risk of huge loss.");
    } else {
        var waiting = "Waiting...";
        var url = '/courierMB/actions/run_computations';
        request("GET", url, null, set_panel_price_and_earnings);
        $_admin_panel_price_for_tour.text(waiting);
        $_admin_panel_total_earnings.text(waiting);
        $_admin_panel_earnings_from_packages.text(waiting);
        console.log("Run computations has been called")
    }
}

//perform adding packages to the database
function add_to_database() {
    var add_to_database_url = '/courierMB/actions/add_to_database/';
    user_input_value = $_admin_panel_add_packages_input.val();
    if (user_input_value){
        user_input_value = parseInt(user_input_value);
        if (user_input_value > 0){
            var number_of_packages_obj = {number_of_packages : user_input_value};
            request("POST", add_to_database_url, number_of_packages_obj, update_database_status);
        }
    }
}

function remove_packages(){
    packs_to_delete = $_admin_panel_remove_packages_input.val();
    var remove_packages_url = '/courierMB/actions/remove_packages/';
    var packages_to_remove = {packs_to_delete : packs_to_delete};
    request("post", remove_packages_url, packages_to_remove, update_database_status);
}

function update_database_status(status){
    $_admin_panel_packages_status.text(status.num_of_packs);
}

function clear_database(){
    var clear_packages_table_url = '/courierMB/actions/clear_database/';
    request("GET", clear_packages_table_url, null, update_database_status);
}

function set_panel_price_and_earnings(data){
    $_admin_panel_price_for_tour.text(data.value + " " + "€");
    $_admin_panel_earnings_from_packages.text(data.earnings_from_packages + " " + "€");
    $_admin_panel_total_earnings.text(data.total_earnings + " " + "€");
    $_admin_panel_trip_order.text(data.best_trip)
}




