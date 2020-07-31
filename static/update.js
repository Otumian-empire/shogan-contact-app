$(document).ready(function () {

    $.ajax({
        url: "http://127.0.0.1:5000/api/",
        dataType: "json",
        method: "GET",
        success: function (res) {
            var data = res['data']
            var status = res['status']
            var rows = ''

            if (status) {
                for (var i = 0; i < data.length; i++) {
                    rows += "<tr>"
                    rows += "<th scope='row'>" + data[i]['id'] + "</th>"
                    rows += "<td>" + data[i]['name'] + "</td>"
                    rows += "<td>" + data[i]['number'] + "</td>"

                    rows += "<td>"
                    rows += '<a class="btn btn-success" href="http://127.0.0.1:5000/web/update/' + data[i]["id"] + '"><i class="fas fa-edit">E</i></a>'
                    rows += '<a class="btn btn-danger" href="http://127.0.0.1:5000/web/delete/' + data[i]["id"] + '"><i class="far fa-trash-alt">D</i></a>'
                    rows += '</td>'
                    rows += "</tr>"
                }
                $("#tableBody").append(rows)
            } else {
                console.log("there was an error")
            }
        },
        error: function (err) {
            console.log(err)
        }
    })


})
