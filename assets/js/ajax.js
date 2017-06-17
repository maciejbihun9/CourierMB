function request(type, url, data, callback_func){
    $.ajax({
        url: url,
        type: type,
        data: JSON.stringify(data),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        async: true,
        success: function(data) {
            callback_func(data)
        }
    });
}
