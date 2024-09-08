import mysql.connector
import streamlit as st

#connec
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='sql123',
    database='crud'
)
#cursor
cur=mydb.cursor()

def main():
    st.title("CRUD OPERATIONS")
    choice=st.sidebar.selectbox("",('CREATE','READ','UPDATE','DELETE'))

    match choice:
        case 'CREATE':
            st.subheader('Insert a record')
            name = st.text_input('Enter name')
            email= st.text_input('Enter email')
            try:
                if st.button('Insert'):
                    query='INSERT INTO users(name,email) VALUES(%s,%s)'
                    val=(name,email)
                    cur.execute(query,val)
                    mydb.commit()
                    st.success('Record inserted !!')
            except Exception:
                st.write('Enter data properly')


        case 'READ':
            st.subheader('Read records')
            if st.button('Get all users'):
                cur.execute('select * from users')
                res=cur.fetchall()
                for row in res:
                    row=str(row).strip("()")
                    st.text(row)
            
            id=st.text_input('Enter ID')
            but=st.button('Get a specific user')
            val=(id,)   
            if but:

                cur.execute('select * from users where id=%s',val)
                res=cur.fetchall()
                for row in res:
                    row=str(row).strip("()")
                    st.text(row)



        case 'UPDATE':
            st.subheader('Update a record')
            id=st.text_input('Enter ID')
            name=st.text_input('Enter new name')
            email=st.text_input('Enter new email')
            if st.button('Update'):
                val=(name,email,id)
                cur.execute('update users set name=%s,email=%s where id=%s',val)
                mydb.commit()
                st.success("Record updates succesfully")
                #val=(name,email,id)

        case 'DELETE':
            st.subheader('Delete a record')
            id=st.text_input('Enter userID to delete')
            val=(id,)
            if st.button('Delete this user'):

                cur.execute('delete from users where id=%s',val)
                st.success('record deleted succesfully !!')
                mydb.commit()
                cur.execute('select * from users')
                res=cur.fetchall()
                for row in res:
                    st.write(row)


if __name__ =='__main__' :
    main()