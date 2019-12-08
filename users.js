db.createUser({
    user: "namos",
    pwd: "namosPass",
    roles:[{role: "readWrite" , db:"namos"}]
})


db.grantRolesToUser( "namos", ["readWrite"] )