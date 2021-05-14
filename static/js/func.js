function delete_lines(id, e, url_delete){
  Swal.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, delete it!'
}).then((result) => {
  if (result.isConfirmed) {
     $.ajax({
        url: url_delete,
            data: {
              'id': id
            },
        dataType: 'json',
          success: function (data) {
             if(data.delete == 1){
                Swal.fire(
                  'Deleted!',
                  'Your item has been deleted.',
                  'success'
                )
               $(`#${id}`).closest('tr').remove()
             }
            
          }
       })    
    }
  })
}
function confirmDelivery(id, e, url_delete){
  Swal.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'info',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, Confirm it!'
}).then((result) => {
  if (result.isConfirmed) {
     $.ajax({
        url: url_delete,
            data: {
              'id': id
            },
        dataType: 'json',
          success: function (data) {
             if(data.delete == 1){
                Swal.fire(
                  'Confirmed!',
                  'Your item has been confirmed.',
                  'success'
                )
               $(`#${id}`).closest('tr').remove()
             }
            
          }
       })    
    }
  })
}