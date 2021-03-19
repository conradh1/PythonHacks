#include <Python.h>
//#include <python1.5/rename2.h>

main(argc, argv)
int argc;
char **argv;
{
    /* This is the simplest embedding mode.  */
    /* Other API functions return results,   */
    /* accept namespace arguments, allow     */
    /* access to real Python objects, etc.   */
    /* Strings may be precompiled for speed. */

    Py_Initialize();                                     /* initialize python */
    PyRun_SimpleString("print 'Hello embedded world!'"); /* run  python code */

    /* use C extension module above */
    PyRun_SimpleString("from environ import *");
    PyRun_SimpleString(
           "for i in range(5):\n"
                "\tprint i,\n"
                "\tprint 'Hello, %s' % getenv('USER')\n\n" );

    PyRun_SimpleString("print 'Bye embedded world!'");
}

char *Py_GetProgramName() { return "embed"; }    /* not always needed */