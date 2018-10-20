var cursor = db.questionnaire_questionnairescore.aggregate([
    {
        "$match": {
            "created_at": {'$gte': ISODate("2018-10-20T00:00:00Z"), '$lte': ISODate("2018-10-20T23:59:59Z")},
        }
    },
    {
        $lookup: {
            from: "users_userprofile",
            localField: "user_id",
            foreignField: "_id",
            as: "user"
        }
    },
    {$unwind: "$user"},
    {$addFields: {name: "$user.name", mobile: "$user.mobile"}},
    {
        $lookup: {
            from: "users_userprofile",
            localField: "consultant_email",
            foreignField: "email",
            as: "consultant"
        }
    },
    {$unwind: "$consultant"},
    {$addFields: {consultant_name: "$consultant.name", consultant_mobile: "$consultant.mobile"}},
    {
        $project: {
            _id: 0,
            name: 1,
            mobile: 1,
            category: 1,
            value: 1,
            consultant_name: 1,
            consultant_mobile: 1
        }
    }
]);

if (cursor && cursor.hasNext()) {
    print('姓名,手机号,测试类型,得分,咨询师姓名,咨询师手机号');
    while (cursor.hasNext()) {
        var item = cursor.next();
        var value = item.value.replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/\"/g, "&quot;")
            .replace(/\"/g, "&amp;")
            .replace(/©/g, "&#9;");
        print('"' + item.name + '","' + item.mobile + '","' + item.category + '","' + value + '","' + item.consultant_name + '","' + item.consultant_mobile + '"');
        //printjson(cursor.next()); -- or if you prefer the JSON
    }

}

/**
 * mongodb 命令行查询
 db.getCollection('questionnaire_questionnairescore').aggregate([
 {
        "$match": {
            "created_at": {'$gte': ISODate("2018-09-30T00:00:00Z"), '$lte': ISODate("2018-09-30T23:59:59Z")},
        }
},
 {
  $lookup: {
    from: "users_userprofile",
    localField: "user_id",
    foreignField: "_id",
    as: "user"
  }
},
 {$unwind:"$user"},
 {$addFields:{name:"$user.name", mobile:"$user.mobile"}},
 {
    $lookup: {
    from: "users_userprofile",
    localField: "consultant_email",
    foreignField: "email",
    as: "consultant"
  }},
 {$unwind:"$consultant"},
 {$addFields:{consultant_name:"$consultant.name", consultant_mobile:"$consultant.mobile"}},
 {$project: {
    _id:0,
    name: 1,
    mobile:1,
    category:1,
    value:1,
    consultant_name:1,
    consultant_mobile:1
  }}
 ])

 * linux命令行执行导出查询结果到csv文件
 mongo 127.0.0.1/zhiliangku export.js > aaa.csv --quiet
 /usr/local/mongodb/bin/mongo -u root -p 111111 --authenticationDatabase admin 127.0.0.1/zhiliangku  export.js > aaa.csv --quiet
 **/