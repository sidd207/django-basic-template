  
$(document).ready(function() {
    
    //Select option for state box.
    var numbers = [ "Andhra Pradesh", "Arunachal Pradesh","Assam", "Bihar","Chhattisgarh","Goa",
        "Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
        "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab", "Rajasthan", "Sikkim",
        "Tamil Nadu","Telangana","Tripura","Uttarakhand","Uttar Pradesh","West Bengal","Andaman and Nicobar Islands",
        "Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Delhi", "Lakshadweep","Puducherry"];
    var option = '';
    for (var i=0;i<numbers.length;i++){
        option += '<option value="'+ numbers[i] + '">' + numbers[i] + '</option>';
    }
    $('#state').append(option);

    $('#datatableId tfoot tr').appendTo('#datatableId thead');
    // Setup - add a text input to each footer cell
    $('#example tfoot th').each( function () {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="Search '+title+'" />' );
    } );

    // DataTable
    var oTable = $('#example').DataTable({
        dom: 'Bfrtip',
        buttons: [
            'csv',
        ]
    });

    // Apply the search
    oTable.columns().every( function () {
        var that = this;
        $( 'input', this.footer() ).on( 'keyup change clear', function () {
            if ( that.search() !== this.value ) {
                that
                    .search( this.value )
                    .draw();
            }
        } );
    } );


    $("#create" ).click(function() {
        if($('#state').val() == null || $('#dtype').val() == null ||
            $('#rnumber').val().length == 0 || $('#atype').val() == null){
                $("form").after("<div class='validation' style='color:red;margin-bottom: 20px;'>Please enter all required fields.</div>");
            }else{
                if ( $('#rnumber').val().length > 20){
                    $("form").after("<div class='validation' style='color:red;margin-bottom: 20px;'>Reference Number should be less than 20 digit.</div>");
                }else{
                    $("#codeform" ).submit();
                }
            }
        }
    );     
    
    $('.input-daterange input').each(function() {
        $(this).datepicker('clearDates');
        });

    $("#create-btn").click(function(){
        if($('#1a-content').hasClass('hidden') == true){
            $('#1a-content').removeClass('hidden');
        }
    })

    $("#cancel").click(function(){
        if($('#1a-content').hasClass('hidden') == false){
            $('#1a-content').addClass('hidden');
        }
    })
        

    window.setTimeout(function() {
        $(".alert").fadeTo(500, 0).slideUp(500, function(){
            $(this).remove(); 
        });
    }, 2000);

    $('.tab').on('click', function() {
        //    Remove .active class from all .tab class elements
        $('.tab').removeClass('active');
        //    Add .active class to currently clicked element
        $(this).addClass('active');
    });


    //Date range filter code.
    $('#search').click(function(){

        $.fn.dataTable.ext.search.push(
            function (settings, data, dataIndex) {
                var min = $('#min').datepicker("getDate");
                var max = $('#max').datepicker("getDate");
                var startDate = new Date(data[5]);
                if (min == null && max == null) { return true; }
                if (min == null && startDate <= max) { return true;}
                if(max == null && startDate >= min) {return true;}
                if (startDate <= max && startDate >= min) { return true; }
                return false;
            }
        );

        oTable.draw();
    })

    $("#min, #max").val(null);


} );    