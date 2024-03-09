import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np



def main():
    st.text("This is Adam C")
    st.write("this is **just** a toy in a big **_shop_**")
    dc = {"a": 12, "b": 23, "c":45}
    dc
    # st.write(dc)
    # fig, ax = plt.subplots()
    # ax.scatter(np.arange(5) , np.arange(5) ** 2)
    # st.write(fig)

    # st.write(st.error)
    # st.write()

    code = '''
            def func():
                print(np.arange(10))
            '''
    
    st.code(code, "python")


if __name__ == "__main__":
    main()
