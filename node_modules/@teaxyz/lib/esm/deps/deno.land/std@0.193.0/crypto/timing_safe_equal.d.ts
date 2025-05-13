/** Compare to array buffers or data views in a way that timing based attacks
 * cannot gain information about the platform. */
export declare function timingSafeEqual(a: ArrayBufferView | ArrayBufferLike | DataView, b: ArrayBufferView | ArrayBufferLike | DataView): boolean;
