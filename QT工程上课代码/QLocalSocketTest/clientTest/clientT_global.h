#ifndef CLIENTT_GLOBAL_H
#define CLIENTT_GLOBAL_H

#if defined (CLIENTT_LIBRARY)
# define CLIENTT_EXPORT Q_DECL_EXPORT
#else
# define CLIENTT_EXPORT Q_DECL_IMPORT
#endif

#endif // CLIENTT_GLOBAL_H
