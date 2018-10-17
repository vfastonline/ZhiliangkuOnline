var arrMap = function (arr, i, j) {
  if(arr) {
  return arr.map(function (value, index) {
    var result = value.slice(4, 6);
    if (result > i && result < j) {
      return value;
    }
  });
  }
};


var arrMap2 = function (arr) {
  if(arr) {
  return arr.map(function (value, index) {
    if (value) {
      return value.slice(2, 6) + ':' + value.slice(0, 2);
    }
  });
  }
};


var arrsLice = function (arr) {
  var b = [];
  for (var i = 0; i < arr.length; i++) {
    if (typeof(arr[i]) != 'undefined') {
      b.push(arr[i]);
    }
  }
  return b;
};


var arrs = {
  arrMap,
  arrMap2,
  arrsLice
};

export default arrs
